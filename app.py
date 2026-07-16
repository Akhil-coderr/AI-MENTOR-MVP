# Name: AKHIL C.
# Roll Number: 24BAD007
#  for hosting: streamlit run app.py
import streamlit as st
import os
import json
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field

# 1. Load Environment Variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# 2. Define the Pydantic Schema (Using your exact structure)
class StartupEvaluation(BaseModel):
    viability_score: int = Field(description="An integer between 1 and 100 assessing overall potential.")
    strengths: str = Field(description="A list three of the idea's core advantages.")
    key_risks: str = Field(description="A list of three primary execution or market pitfalls.")
    recommendations: str = Field(description="Exactly two concrete, actionable steps for improvement.")

# 3. System Prompt
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
"and also give me all the points as star points and not numbers"
Maintain a sharp, professional, and encouraging mentor tone. Do not use generic corporate jargon. Be specific to the submitted text.
"""

# 4. Streamlit UI Configuration
st.set_page_config(page_title="Aurstrat AI Mentor", page_icon="💡")
st.title("💡 Aurstrat AI Mentor Proto-App")
st.write("Submit your startup idea below to receive a Venture Capital-grade evaluation.")

# 5. User Input Area (Replacing the terminal input())
student_idea = st.text_area("Enter your student startup idea details:", height=150)

# 6. Action Button & API Call
if st.button("Evaluate Startup Idea"):
    if not student_idea.strip():
        st.warning("Input cannot be empty. Please describe an idea!")
    else:
        # Spinner shows while the API is thinking
        with st.spinner("Analyzing your idea and calculating viability... please wait..."):
            try:
                # Call Gemini API
                response = client.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=student_idea,
                    config={
                        'system_instruction': system_prompt,
                        'response_mime_type': 'application/json',
                        'response_schema': StartupEvaluation,
                        'temperature': 0.25,
                        'top_p': 0.90,
                    }
                )

                # Parse JSON
                evaluation = json.loads(response.text)
                
                # Render Results cleanly on the webpage
                st.divider()
                st.subheader("STARTUP EVALUATION REPORT")
                
                # Print Score
                score = evaluation.get("viability_score", "N/A")
                st.metric(label="📊 OVERALL VIABILITY SCORE", value=f"{score}/100")
                st.divider()
                
                # Print Strengths
                st.write("### ✅ CORE STRENGTHS")
                strengths = evaluation.get("strengths", "")
                if isinstance(strengths, str):
                    strengths = [strengths]
                for item in strengths:
                    for sentence in item.split(". "):
                        if sentence.strip():
                            clean_sentence = sentence.strip().rstrip(".")
                            st.write(f"- {clean_sentence}.")
                    
                # Print Risks
                st.write("### ⚠️ KEY EXECUTION RISKS")
                risks = evaluation.get("key_risks", "")
                if isinstance(risks, str):
                    risks = [risks]
                for item in risks:
                    for sentence in item.split(". "):
                        if sentence.strip():
                            clean_sentence = sentence.strip().rstrip(".")
                            st.write(f"- {clean_sentence}.")
                    
                # Print Actionable Recommendations
                st.write("### 💡 IMMEDIATE STRATEGIC RECOMMENDATIONS (7-14 Day Plan)")
                recommendations = evaluation.get("recommendations", "")
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
                    st.write(f"**{i}.** {rec}")

            except Exception as e:
                st.error(f"An error occurred: {e}")
