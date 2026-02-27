# hiring_assistant



#  TalentScout – AI Hiring Assistant Chatbot

##  Project Overview

TalentScout Hiring Assistant is an AI-powered chatbot developed to streamline the initial screening process for technical candidates. The chatbot interacts with applicants, collects essential details, and dynamically generates technical interview questions based on the candidate's declared tech stack.

This project demonstrates:

* Large Language Model (LLM) integration using Groq API
* Prompt engineering for structured information collection
* Context-aware conversational flow
* Secure handling of candidate data
* Cloud deployment readiness (AWS EC2)

---

#  Objective

To design an intelligent conversational assistant that:

1. Collects structured candidate information
2. Generates tailored technical interview questions
3. Maintains conversational context
4. Handles unexpected input gracefully
5. Provides a seamless user experience

---

#  System Architecture

```
Streamlit UI
      ↓
Conversation Manager (Session Memory)
      ↓
Groq LLM (Llama 3.1)
      ↓
Candidate Data Storage (JSON-based simulation)
```

---

#  Tech Stack

##  Programming Language

* Python 3.10+

## Libraries Used

* streamlit – Frontend interface
* groq – LLM integration
* python-dotenv – Secure API key management
* json – Simulated data storage

##  LLM Model Used

* `llama-3.1-8b-instant` (via Groq API)

---

#  Features Implemented

## 1️ Greeting & Role Introduction

* Professional welcome message
* Explains purpose of the chatbot
* Guides candidate through screening process

---

## 2️⃣ Candidate Information Collection

The chatbot collects:

* Full Name
* Email Address
* Phone Number
* Years of Experience
* Desired Position
* Current Location
* Tech Stack

Structured prompting ensures accurate information capture.

---

## 3️⃣ Dynamic Technical Question Generation

Once the tech stack is declared, the chatbot:

* Identifies listed technologies
* Generates 3–5 technical questions per technology
* Includes scenario-based and real-world questions
* Maintains moderate interview-level difficulty

Example:

If candidate enters:

```
Python, Django, MySQL
```

The chatbot generates:

* Python OOP and memory management questions
* Django ORM and middleware questions
* MySQL indexing and query optimization questions

---

## 4️⃣ Context Management

The application uses Streamlit session state to:

* Maintain full conversation history
* Enable coherent follow-up interactions
* Avoid loss of conversational flow

---

## 5️⃣ Fallback Mechanism

If user input is:

* Unclear
* Irrelevant
* Outside hiring scope

The chatbot:

* Politely requests clarification
* Avoids deviating from its purpose
* Maintains professional tone

---

## 6️⃣ Conversation Termination

If candidate types:

```
exit
quit
bye
```

The chatbot:

* Gracefully concludes
* Thanks the candidate
* Informs about next steps

---

#  Prompt Engineering Strategy

## System Prompt Design

The system prompt enforces:

* Hiring assistant role restriction
* Structured information collection
* Tech-stack-based question generation
* Professional tone control
* Purpose-bound responses

Temperature set to:

```
0.3
```

This ensures:

* Deterministic responses
* Controlled output
* Reduced hallucination

---

## Technical Question Prompt Strategy

Dynamic prompt template:

* Injects declared tech stack
* Forces question count limit
* Encourages scenario-based assessment
* Prevents generic responses

---

#  Data Privacy & Security

## Sensitive Data Handling

* API keys stored in `.env`
* `.env` excluded via `.gitignore`
* No hardcoded secrets
* Simulated backend storage

## Compliance Considerations

* Only simulated candidate data used
* No external database storing real user data
* Designed to follow GDPR best practices

---

#  Installation & Setup

## 1️⃣ Clone Repository

```
https://github.com/Reddy0402/hiring_assistant
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate  (Windows)
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Create .env File

```
GROQ_API_KEY=your_actual_groq_api_key
```

---

## 5️⃣ Run Application

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

#  AWS Deployment (EC2)

The application can be deployed on AWS EC2:

1. Launch Ubuntu EC2 instance
2. Install Python & Git
3. Clone repository
4. Install dependencies
5. Set environment variable:

   ```
   export GROQ_API_KEY="your_key"
   ```
6. Run:

   ```
   streamlit run app.py --server.port 8501 --server.address 0.0.0.0
   ```

Access via:

```
http://your-ec2-public-ip:8501
```

---

# Project Structure

```
talentscout-hiring-assistant/
│
├── app.py                # Streamlit UI & conversation flow
├── llm_handler.py        # Groq API integration
├── prompts.py            # Prompt engineering templates
├── data_store.py         # Simulated data storage
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Challenges Faced & Solutions

## Challenge 1: Maintaining Context

Solution: Used Streamlit session state to store message history.

## Challenge 2: Structured Data Collection

Solution: Designed system prompts enforcing required fields sequentially.

## Challenge 3: Avoiding Off-Topic Responses

Solution: Role-constrained system prompt with purpose restriction.

## Challenge 4: Model Deprecation

Solution: Updated to llama-3.1-8b-instant after decommission notice.

---

#  Future Enhancements

* Sentiment analysis integration
* Multilingual support
* Database integration (PostgreSQL)
* Resume parsing using NLP
* Admin dashboard for recruiters
* Docker containerization


---

#  Evaluation Alignment

This project satisfies:

✔ LLM integration
✔ Prompt engineering
✔ Context management
✔ Structured data collection
✔ Secure key handling
✔ Clean UI implementation
✔ Cloud deployment capability

---

#  Demo

(Optional)

* Loom walkthrough link
* AWS live demo link

---

# Author

Sai Teja Reddy
AI/ML Engineering Student
Specialization: Artificial Intelligence & Machine Learning


