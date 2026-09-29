# 🛡️ ContextGuard
> **An Explainable Deep Learning System for Detecting Context Collapse in Digital Content**  
> *Department of Computer Science & Engineering, Bangalore Institute of Technology (BIT)*  
> *Minor Project (BCS586) — V Semester 2026–2027*

---

## 🎯 Project Overview
ContextGuard detects when a genuine statement becomes misleading because its original
context has been removed, exaggerated, contradicted, or numerically distorted.

**Core Question:** *"Does this content faithfully represent the meaning and context of its source?"*

---

## 📂 Repository Structure & Workspaces

The repository is structured with dedicated workspaces for each team member:

```text
CONTEXT-GUARD/
│
├── 🧠 ml_nlp/                   ← Member 1: ML / NLP Workspace
│   ├── transformer/
│   ├── embeddings/
│   └── classifier/
│
├── 📚 data_retrieval/           ← Member 2: Data & Retrieval Workspace
│   ├── dataset/
│   ├── retrieval/
│   └── vector-search/
│
├── ⚙️ backend/                  ← Member 3: Backend Workspace
│   ├── fastapi/
│   ├── database/
│   └── authentication/
│
├── 🎨 frontend/                 ← Member 4: Frontend UI Workspace
│   ├── react/
│   ├── upload/
│   └── dashboard/
│
├── 📋 TEAM_WORKFLOW.md          ← Git branching & collaboration guide
├── requirements.txt             ← Python dependencies
└── Dockerfile                   ← Containerization
```

---

## 🌿 Git Branches

Each member works on their dedicated branch:
* `main`: Protected base
* `member1-ml`: Member 1 (ML / NLP)
* `member2-retrieval`: Member 2 (Data & Retrieval)
* `member3-backend`: Member 3 (Backend)
* `member4-frontend`: Member 4 (Frontend)
