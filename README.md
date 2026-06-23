# Enterprise Multi-Source RAG Knowledge Platform

A production-style Retrieval-Augmented Generation (RAG) platform capable of answering questions from multiple enterprise data sources including documents and structured datasets.

---

## Overview

This project demonstrates how modern enterprise AI systems retrieve relevant information from internal knowledge bases using semantic search and vector databases.

The system supports:

- PDF/Text documents
- CSV datasets
- Semantic retrieval with FAISS
- Hybrid search
- Multi-stage retrieval with reranking
- Conversation memory
- Query analytics
- FastAPI APIs
- Docker deployment

---

## Features

### Multi-Source Knowledge Ingestion
- Employee documents
- Company policies
- Cloud architecture guides
- Employee databases
- Product databases
- Support ticket datasets

### Retrieval Pipeline
- Document chunking
- TF-IDF embeddings
- FAISS vector search
- Hybrid retrieval
- Multi-stage retrieval
- Reranking

### Contextual Question Answering
- Citation-based responses
- Conversation memory
- Session tracking
- Persistent chat history

### Production Features
- FastAPI backend
- Docker support
- Query logging
- Analytics export
- Cache system

### Evaluation Framework
- Precision@K
- Recall@K
- Retrieval Accuracy
- Benchmark dataset

---

# Project Architecture

User Query
↓
Embedding Generation
↓
FAISS Vector Search
↓
Hybrid Retrieval
↓
Reranking
↓
Best Context Selection
↓
Answer + Source Citation

---

# Tech Stack

| Category | Technologies |
|------------|-------------|
| Language | Python |
| API | FastAPI |
| Vector Database | FAISS |
| Search | Semantic Search + Hybrid Search |
| ML | Scikit-Learn |
| Database | SQLite (PostgreSQL concepts) |
| Deployment | Docker |
| Storage | Pickle |
| Analytics | Pandas |
| Evaluation | Precision@K, Recall@K |

---

# Project Structure

```text
Enterprise Multi-Source RAG Knowledge Platform/

│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── documents.pkl
│   ├── chunks.pkl
│   ├── embeddings.npy
│   ├── faiss_index.bin
│   ├── metadata.pkl
│   ├── vectorizer.pkl
│   ├── session_memory.pkl
│   ├── query_logs.db
│   │
│   ├── text_docs/
│   ├── csv/
│   └── pdfs/
│
├── outputs/
│   ├── query_analytics.csv
│   ├── evaluation_metrics.csv
│   └── reranking_results.csv
│
├── Notebook 1 - Data Ingestion.ipynb
├── Notebook 2 - Chunking.ipynb
├── Notebook 3 - Embeddings + FAISS Vector Database.ipynb
├── Notebook 4 - RAG Question Answering Pipeline.ipynb
├── Notebook 5 - Conversation Memory + Chat History.ipynb
├── Notebook 6 - FastAPI Backend.ipynb
├── Notebook 7 - Docker + Project Structure.ipynb
├── Notebook 8 - Hybrid Search.ipynb
├── Notebook 9 - Cache + Session Memory.ipynb
├── Notebook 10 - Query Logging + Analytics.ipynb
├── Notebook 11 - Evaluation Metrics.ipynb
└── Notebook 12 - Reranking + Multi-Stage Retrieval.ipynb
```

---

# Dataset

### Documents

- employee_handbook.txt
- company_policies.txt
- cloud_migration_guide.txt

### Structured Data

#### employees.csv

Contains:

- Employee ID
- Department
- Experience

#### products.csv

Contains:

- Product information
- Categories
- Pricing

#### support_tickets.csv

Contains:

- Ticket IDs
- Priority levels
- Issues

---

# Notebooks

## Notebook 1
Data ingestion and dataset creation.

## Notebook 2
Document chunking.

## Notebook 3
Embedding generation and FAISS index creation.

## Notebook 4
RAG question-answering pipeline.

## Notebook 5
Conversation memory and chat history.

## Notebook 6
FastAPI backend.

## Notebook 7
Docker configuration and project organization.

## Notebook 8
Hybrid search implementation.

## Notebook 9
Cache system and session memory.

## Notebook 10
Query logging and analytics.

## Notebook 11
Evaluation metrics and retrieval benchmarking.

## Notebook 12
Multi-stage retrieval and reranking.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Enterprise-Multi-Source-RAG-Knowledge-Platform.git

cd Enterprise-Multi-Source-RAG-Knowledge-Platform
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run FastAPI

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Example Questions

### How many leave days are allowed?

Answer:

```
Employees receive 20 annual leave days.
```

Source:

```
employee_handbook.txt
```

---

### Who works in ML Engineering?

Answer:

```
Bob works in ML Engineering.
```

Source:

```
employees.csv
```

---

### What monitoring tools are used?

Answer:

```
Prometheus and Grafana are used for monitoring.
```

Source:

```
cloud_migration_guide.txt
```

---

# Evaluation Results

Metrics implemented:

- Precision@K
- Recall@K
- Retrieval Accuracy

These metrics help benchmark retrieval quality and improve response relevance.

---

# Resume Highlights

- Built a production-grade Retrieval-Augmented Generation platform supporting multiple enterprise data sources.
- Implemented semantic retrieval using FAISS vector search and hybrid retrieval techniques.
- Added session memory, caching, query analytics, and citation-based responses.
- Developed FastAPI APIs and containerized the application using Docker.
- Evaluated retrieval quality using Precision@K, Recall@K, and accuracy metrics.
- Implemented multi-stage retrieval and reranking for improved answer quality.

---

# Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- FAISS
- FastAPI
- Hybrid Search
- Multi-Stage Retrieval
- Query Analytics
- Docker
- Evaluation Metrics
- Information Retrieval
- NLP
- Machine Learning
- Production AI Systems

---

## Future Improvements

- LangChain integration
- Pinecone vector database
- PostgreSQL backend
- Redis caching
- Cross-Encoder reranking
- OpenAI API integration
- Streamlit frontend

---

## License

MIT License
