# ACKO Insurance AI Platform

An end-to-end AI-powered insurance assistant platform built using FastAPI, Gemini API, RAG, Machine Learning, PostgreSQL, ChromaDB, and AWS.

---

# Project Overview

This platform provides AI-powered assistance for both customers and admin users in an insurance system.

The system contains:
- Document RAG for policy Q&A
- Machine Learning for premium prediction
- Gemini Vision for claim analysis
- SQL RAG for admin analytics
- AI Router for intelligent query routing

---

# Features

## User Portal
- Policy Q&A Assistant
- Insurance Premium Quote Prediction
- Claim Filing & Damage Analysis
- Health Insurance Support

## Admin Portal
- Claims Dashboard
- Business Analytics
- SQL AI Assistant
- Customer Insights

---

# Tech Stack

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- FastAPI
- Python

## AI / ML
- Gemini API
- RAG
- LangChain
- Machine Learning

## Databases
- PostgreSQL
- ChromaDB

## Cloud
- AWS EC2
- AWS S3

---

# Project Architecture

Frontend (HTML/CSS/JS)
↓
FastAPI Backend
↓
Main Router / AI Orchestrator
↓
-----------------------------------------
|           |            |             |
SQL RAG   PDF RAG    ML Model    Claim Vision
↓           ↓            ↓             ↓
PostgreSQL ChromaDB   Pickle       Gemini Vision
            ↓
        Gemini API

---

# Folder Structure

acko-insurance-ai/
│
├── frontend/
├── backend/
├── rag/
│   ├── pdf_rag/
│   ├── sql_rag/
│
├── ml_models/
├── database/
├── chroma_db/
├── uploads/
├── docs/
│
├── app.py
├── main.py
├── requirements.txt
└── .env

---

# Modules

## Module 1 — Document RAG
- Policy Q&A chatbot using insurance PDFs

## Module 2 — ML Prediction
- Insurance premium prediction

## Module 3 — Claim Analysis
- Damage analysis using image input

## Module 4 — Dashboard
- Admin analytics dashboard

## Module 5 — SQL RAG
- Natural language to SQL assistant

---

# Future Deployment
- AWS EC2
- AWS S3
- PostgreSQL
