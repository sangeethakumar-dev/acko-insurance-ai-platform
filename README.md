# ACKO Insurance AI Platform

An AI-powered Insurance Management Platform built using FastAPI, Machine Learning, Google Gemini, PostgreSQL and ChromaDB.

---

## Features

### Customer Portal

- Customer Login & Registration
- AI Insurance Assistant
- PDF Policy Chatbot (RAG)
- Bike Insurance Premium Prediction
- Car Insurance Premium Prediction
- Health Insurance Premium Prediction
- AI Claim Submission
- Customer Dashboard

---

### Admin Portal

- Admin Login
- SQL RAG Assistant
- Natural Language → SQL
- Dashboard APIs
- Claim Management APIs
- Policy Management APIs

---

## AI Modules

### Module 1 — PDF RAG

- PDF Loader
- Custom Chunking
- Google Gemini Embeddings
- ChromaDB
- Similarity Search
- Gemini Answer Generation

---

### Module 2 — ML Premium Prediction

Supports

- Bike Insurance
- Car Insurance
- Health Insurance

Workflow

User Input
↓

ML Model
↓

Premium Prediction
↓

Gemini Explanation

---

### Module 3 — AI Claim Engine

- Upload Vehicle Images
- Image Analysis
- Damage Detection
- Fraud Risk Estimation
- Repair Cost Estimation

---

### Module 4 — Customer Frontend

HTML

CSS

JavaScript

Responsive Dashboard

Interactive AI Assistant

---

### Module 5 — SQL RAG

Admin only

Natural Language

↓

Gemini

↓

SQL Query

↓

PostgreSQL

↓

Answer

---

## Tech Stack

Frontend

- HTML
- CSS
- JavaScript

Backend

- FastAPI
- Python

AI

- Google Gemini
- RAG
- ChromaDB

Machine Learning

- Scikit-Learn
- Joblib
- Pandas

Database

- PostgreSQL

---

## Folder Structure

frontend/

backend/

routes/

rag/

ml/

claim_engine/

database/

management/

utils/

uploads/

docs/

chroma_db/

---

## Current Status

✅ PDF RAG Completed

✅ ML Premium Prediction Completed

✅ SQL RAG Completed

✅ AI Claim Backend Completed

✅ Customer Frontend Completed

✅ Authentication Completed

⚠ Gemini API quota exhausted during final integration.

⚠ AWS Deployment Pending.

---

## Future Improvements

- Deploy on AWS EC2
- Store vectors in production vector database
- AWS RDS
- AWS S3
- CI/CD
- Docker