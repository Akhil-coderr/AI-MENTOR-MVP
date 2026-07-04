# AI Mentor MVP
# **PROTOTYPE LINK:** https://ai-mentor-mvp-akhil.streamlit.app/
## Overview

AI Mentor MVP is a prototype developed for the **Aurstrat Technology AI/ML Internship Assessment**.

The application evaluates a student's startup idea (approximately 200 words) using **Prompt Engineering** with a **Large Language Model (LLM) API** and generates structured feedback.

---

## Problem Statement

The AI Mentor analyzes a student's startup idea and returns structured feedback containing:

* Startup Viability Score
* Key Strengths
* Key Risks
* Two Actionable Recommendations

The response is returned in **JSON** format.

---

## Project Objective

The objective of this assessment is to identify and implement the most suitable AI approach under the given startup constraints:

* Limited engineering resources
* Near-zero infrastructure budget
* Small development team
* MVP delivery within two weeks
* Easy maintenance and scalability

After evaluating the available approaches, this prototype implements **Prompt Engineering using an existing LLM API**.

---

## Features

* Accepts a startup idea as input
* Uses Prompt Engineering with an LLM API
* Generates structured startup feedback
* Returns the response in JSON format

---

## Architecture Decision

Three approaches were evaluated:

* Fine-tuning
* Retrieval-Augmented Generation (RAG)
* Prompt Engineering

Based on the assessment constraints, **Prompt Engineering** was selected due to its low cost, fast development, minimal infrastructure, and ease of maintenance.

A detailed comparison is included in the **Architecture Decision Report**.

---

## Technology Stack

* Python
* Large Language Model (LLM) API
* Prompt Engineering
* JSON

---

## How It Works

1. The user enters a startup idea.
2. A structured prompt is sent to the LLM API.
3. The model analyzes the idea.
4. Structured feedback is returned in JSON format.

---

## Limitations

* Response quality depends on the prompt and user input.
* Responses may vary between API calls.
* Domain-specific business insights may not always be accurate.

---

## Future Improvements

* Integrate RAG for domain-specific knowledge.
* Refine prompt design.
* Add personalized mentoring.
* Build a simple web interface.

---

## AI Usage Declaration

This project was developed with the assistance of AI tools for research, brainstorming, documentation, and implementation support. All architectural decisions and implementation choices were reviewed and validated by the author.
