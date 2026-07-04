# python -m venv venv
# venv\Scripts\activate

import os
import json
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field

# 1. Load the secret API key from the .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Initialize the Gemini Client
client = genai.Client(api_key=api_key)

# 3. Define the strict JSON structure using Pydantic (This enforces our ADR requirements!)
class StartupEvaluation(BaseModel):
    viability_score: int = Field(description="An integer between 1 and 100 assessing overall potential.")
    strengths: str = Field(description="A list of the idea's core advantages.")
    key_risks: str= Field(description="A list of primary execution or market pitfalls.")
    recommendations: str= Field(description="Exactly two concrete, actionable steps for improvement.")

# 4. The System Prompt (Instructions for the AI)
system_prompt = """
You are an elite startup incubator director, venture capital analyst, and empathetic business mentor. 
Your job is to provide highly critical yet constructive feedback on startup ideas submitted by students.

Follow these analytical guidelines strictly:
1. CRITICAL ANALYSIS: Look past the surface level. Assess unit economics, user acquisition hurdles, operational bottlenecks, scaling obstacles, and hidden market dependencies.
2. CONTEXTUAL SCORING: Evaluate the 'viability_score' relative to the intended scale of the idea:
   - For hyper-local or small-scale community projects (e.g., a dorm service), grade them on execution ease, local utility, and self-sustainability. Do not penalize them for not being global tech giants.
   - For venture-scale tech ideas, grade them rigorously on market size, defensive moats, and scalability.
3. STRENGTHS: Focus on unique insights, clear immediate value propositions, low barriers to initial entry, or organic community-driven growth loops.
4. KEY RISKS: Identify real vulnerabilities. Think about free-rider issues, human behavior failures, legal/compliance blocks, financial mismanagement, or customer churn.
5. RECOMMENDATIONS BOUNDARY: You MUST provide EXACTLY TWO distinct, concrete, and highly actionable recommendations. They must be practical next steps that a student can complete within 7-14 days without a massive budget (e.g., building a specific landing page, creating a specific survey, running a manual test with 10 users).

Maintain a sharp, professional, and encouraging mentor tone. Do not use generic corporate jargon. Be specific to the submitted text.
"""
print("=" * 60)
print("          WELCOME TO THE AURSTRAT AI MENTOR PROTO-APP        ")
print("=" * 60)
print("Type 'exit' at any time to close the application.\n")

# --- Interactive Evaluation Loop ---
while True:
    print("-" * 60)
    # Get the startup idea live from the user terminal
    student_idea = input("Enter your student startup idea details:\n> ")
    print("-" * 60)
    
    # Check if the user wants to break out of the app
    if student_idea.strip().lower() == 'exit':
        print("\nThank you for using Aurstrat AI Mentor. Goodbye!")
        break
        
    # Skip empty submissions
    if not student_idea.strip():
        print("Input cannot be empty. Please describe an idea!")
        continue

    print("\n[AI MENTOR] Analyzing your idea and calculating viability... please wait...\n")

    # 6. Call the Gemini API with Structured Output and tuned parameters
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=student_idea,
            config={
                'system_instruction': system_prompt,
                'response_mime_type': 'application/json',
                'response_schema': StartupEvaluation,
                
                # --- New Tuning Parameters ---
                'temperature': 0.25,          # Low randomness for strict, analytical feedback
                'top_p': 0.90,                # Keeps vocabulary choices grounded
            }
        )

        # 7. Parse the JSON and display it as a beautifully formatted Report
        evaluation = json.loads(response.text)
        
        print("=" * 60)
        print("                STARTUP EVALUATION REPORT   ")
        print("=" * 60)
        
        # Print Score
        score = evaluation.get("viability_score", "N/A")
        print(f"\n OVERALL VIABILITY SCORE: {score}/100")
        print("-" * 60)
        
        # Print Strengths
        print("\n CORE STRENGTHS:")
        strengths = evaluation.get("strengths", [])
        # BUG FIX: If the AI returns a single string, wrap it in a list so Python doesn't loop through individual letters
        if isinstance(strengths, str):
            strengths = [strengths]
            
        for item in strengths:
            for sentence in item.split(". "):
                if sentence.strip():
                    clean_sentence = sentence.strip().rstrip(".")
                    print(f"  • {clean_sentence}.")
                    
        # Print Risks            
        print("\n KEY EXECUTION RISKS:")
        risks = evaluation.get("key_risks", [])
        if isinstance(risks, str):
            risks = [risks]
            
        for item in risks:
            for sentence in item.split(". "):
                if sentence.strip():
                    clean_sentence = sentence.strip().rstrip(".")
                    print(f"  • {clean_sentence}.")
                    
        # Print Actionable Recommendations            
        print("\nIMMEDIATE STRATEGIC RECOMMENDATIONS (7-14 Day Plan):")
        recommendations = evaluation.get("recommendations", [])
        if isinstance(recommendations, str):
            recommendations = [recommendations]
        
        rec_list = []
        for item in recommendations:
            parts = item.replace("\n2.", "||").replace("2. ", "||").split("||")
            for part in parts:
                if part.strip():
                    clean_part = part.strip().lstrip("1234567890. ")
                    rec_list.append(clean_part)
                    
        for i, rec in enumerate(rec_list[:2], 1):
            print(f"\n  {i}. {rec}")
            
        print("\n" + "=" * 60)

    except Exception as e:
        print(f"An error occurred: {e}")