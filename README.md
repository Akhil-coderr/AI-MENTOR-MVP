# AI Mentor MVP

## Overview

AI Mentor MVP is a lightweight prototype developed as part of the **Aurstrat Technology AI/ML Internship Assessment**.

The application evaluates a student's startup idea (approximately 200 words) using **Prompt Engineering** with a **Large Language Model (LLM) API** and generates structured feedback to assess the idea.

The primary objective of this project is to demonstrate practical AI engineering, architecture decision-making, and rapid MVP development under real-world startup constraints.

---

## Problem Statement

Students submit a startup idea describing their business concept. The AI Mentor analyzes the submission and provides structured feedback containing:

* Startup Viability Score
* Key Strengths
* Key Risks
* Two Actionable Recommendations

The response is returned in a structured JSON format for easy processing and integration.

---

## Project Objective

The goal of this assessment is not to build the most advanced AI system, but to identify and implement the most suitable AI approach under the following constraints:

* Limited engineering resources
* Near-zero infrastructure budget
* Small development team with limited ML expertise
* MVP expected within two weeks
* Solution should be easy to maintain and scale

After evaluating the available approaches, this prototype implements **Prompt Engineering using an existing LLM API**.

---

## Features

* Accepts a startup idea as input
* Uses Prompt Engineering to guide the LLM
* Generates structured startup evaluation
* Returns the response in JSON format
* Provides:

  * Startup Viability Score
  * Key Strengths
  * Key Risks
  * Two Actionable Recommendations

---

## Architecture Decision

Three implementation approaches were evaluated:

* Fine-tuning
* Retrieval-Augmented Generation (RAG)
* Prompt Engineering

Based on the business constraints provided in the assessment, **Prompt Engineering** was selected because it offers:

* Fast development
* Low infrastructure requirements
* Minimal operational cost
* Easy maintenance
* Rapid MVP delivery

A detailed comparison and justification are provided in the **Architecture Decision Report**.

---

## Technology Stack

* Python
* Large Language Model (LLM) API
* Prompt Engineering
* JSON
* Environment Variables (`.env`)

---

## How It Works

1. The user enters a startup idea.
2. A structured prompt is generated based on the input.
3. The prompt is sent to the LLM API.
4. The model analyzes the startup idea.
5. Structured feedback is returned in JSON format, including:

   * Startup Viability Score
   * Key Strengths
   * Key Risks
   * Two Actionable Recommendations

---

## Limitations

* The quality of the response depends on the quality of the prompt and user input.
* Responses may vary across different API calls.
* The model may not always capture highly domain-specific business challenges.
* The generated feedback should be treated as guidance rather than professional business advice.

---

## Future Improvements

* Integrate Retrieval-Augmented Generation (RAG) for domain-specific knowledge.
* Improve prompt design through iterative testing.
* Support personalized mentoring based on user profiles.
* Add evaluation metrics to measure response quality.
* Develop a user-friendly web interface.

---

## AI Usage Declaration

This project was developed with the assistance of AI tools for research, brainstorming, documentation, and implementation support. All architectural decisions, implementation choices, testing, and final submission were reviewed and validated by the author.

---

## License

This project was created solely for the **Aurstrat Technology AI/ML Internship Assessment** and is intended for educational and evaluation purposes.
