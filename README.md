AI Mentor MVP
Overview

AI Mentor MVP is a lightweight prototype developed as part of the Aurstrat Technology AI/ML Internship Assessment.

The application evaluates a student's startup idea (approximately 200 words) using Prompt Engineering with a Large Language Model (LLM) API and generates structured feedback to help assess the idea.
Problem Statement

Students submit a startup idea describing their business concept. The AI Mentor analyzes the submission and provides structured feedback containing:

Startup Viability Score
Key Strengths
Key Risks
Two Actionable Recommendations

The response is returned in a structured JSON format for easy processing and integration.

Project Objective

The goal of this assessment is not to build the most advanced AI system, but to identify and implement the most suitable AI approach under the following constraints:

Limited engineering resources
Near-zero infrastructure budget
Small development team with limited ML expertise
MVP expected within two weeks
Solution should be easy to maintain and scale

After evaluating the available approaches, this prototype implements Prompt Engineering using an existing LLM API.

Features
Accepts a startup idea as input
Uses Prompt Engineering to guide the LLM
Generates structured startup evaluation
Returns JSON output
Provides:
Startup Viability Score
Strengths
Risks
Actionable Recommendations
Demonstrates the solution using multiple startup ideas
Architecture Decision

Three implementation approaches were evaluated:

Fine-tuning
Retrieval-Augmented Generation (RAG)
Prompt Engineering

Based on the business constraints provided in the assessment, Prompt Engineering was selected because it offers:

Fast development
Low infrastructure requirements
Minimal operational cost
Easy maintenance
Rapid MVP delivery

A detailed comparison and justification are provided in the Architecture Decision Report.

Technology Stack
Python
Large Language Model (LLM) API
Prompt Engineering
JSON Output
Environment Variables (.env)
How It Works
User enters a startup idea.
The application constructs a structured prompt.
The prompt is sent to the LLM API.
The model evaluates the startup idea.
A structured JSON response is returned containing:
Startup Viability Score
Strengths
Risks
Recommendations

Testing

The prototype was tested using multiple startup ideas from different domains to evaluate the consistency and structure of the generated responses.

Limitations

This prototype is intended as an MVP and has several limitations:

Results depend on the quality of the input prompt.
Responses may vary between API calls.
The model may not always identify domain-specific business challenges accurately.
The generated feedback should be treated as guidance rather than professional business advice.
Future Improvements
Add Retrieval-Augmented Generation (RAG) for domain-specific knowledge.
Support personalized mentoring based on user profiles.
Improve prompt design through iterative testing.
Add evaluation metrics for response quality.
Build a web interface for improved usability.

AI Usage Declaration

This project was developed with the assistance of AI tools for research, brainstorming, documentation, and implementation support. All architectural decisions, implementation choices, testing, and final submission were reviewed and validated by the author.
