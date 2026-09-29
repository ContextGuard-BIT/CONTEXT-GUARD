# ContextGuard — Team Collaboration & Workflow Guide

> **Project:** ContextGuard: An Explainable Deep Learning System for Detecting Context Collapse in Digital Content  
> **Course:** Minor Project (BCS586) — Department of CSE, Bangalore Institute of Technology  
> **Team Size:** 4 Members  

---

## 1. Team Roles & File Ownership Matrix

To prevent merge conflicts and ensure everyone has distinct, demonstrable work for evaluations, each member has **exclusive primary ownership** of specific modules and folders:

| Member | Primary Role | Primary Code Ownership | Secondary / Shared |
|---|---|---|---|
| **Member 1** | **ML / NLP Engineer** | `backend/modules/semantic.py`<br>`backend/modules/classifier.py`<br>`notebooks/` | `backend/tests/` |
| **Member 2** | **Data & Retrieval Engineer** | `backend/modules/retriever.py`<br>`backend/modules/claim_extractor.py`<br>`data/` | `data/sample_pairs.json` |
| **Member 3 (YOU)** | **Backend & Systems Engineer** | `backend/main.py`<br>`backend/api/`<br>`backend/database/`<br>`backend/modules/ocr.py`<br>`Dockerfile`, `docker-compose.yml` | `backend/config.py` |
| **Member 4** | **Frontend Engineer** | `frontend/`<br>`backend/static/` | UI assets & mock payloads |

### ⚠️ Golden Rule of File Ownership:
* If you need a change in a file owned by another member, **open an issue or message them** instead of directly modifying their file on your branch. This guarantees zero Git merge conflicts.

---

## 2. Git Branching Strategy

Our repository uses a protected `main` branch and dedicated feature branches for each member:

```text
main  (Production-ready, tested code only)
 │
 ├── branch: member1-ml         (Transformer fine-tuning, NLI, scoring head)
 ├── branch: member2-retrieval  (FAISS vector search, NER, dataset ingestion)
 ├── branch: member3-backend    (FastAPI endpoints, Database models, OCR, Docker)
 └── branch: member4-frontend   (React components, upload widgets, dashboard)
```

### Daily Git Routine for Every Member:

#### Starting work (Morning):
```bash
# 1. Switch to your branch
git checkout member3-backend

# 2. Pull latest approved changes from main
git pull origin main
```

#### Saving work (Evening):
```bash
# 1. Stage and commit your changes
git add .
git commit -m "feat(backend): add database history endpoint and queries"

# 2. Push to your branch on GitHub
git push origin member3-backend
```

#### Merging into `main`:
* Never push directly to `main`.
* Go to GitHub ➔ Open a **Pull Request (PR)** from `memberX-...` into `main`.
* At least 1 other team member must review and approve.
* All unit tests (`pytest backend/tests/ -v`) must pass before merging.

---

## 3. GitHub Projects (Kanban Board) Setup

Set up a free **GitHub Project** on the repository with these 4 columns:

```
┌───────────────┐   ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│  📋 BACKLOG   │ ➔ │ 🔨 IN PROGRESS│ ➔ │  👀 IN REVIEW │ ➔ │    ✅ DONE    │
└───────────────┘   └───────────────┘   └───────────────┘   └───────────────┘
```

### Initial Task Distribution for the Board:

#### Member 1 (ML / NLP):
- [ ] Task 1.1: Test DeBERTa cross-encoder on all 5 context collapse categories.
- [ ] Task 1.2: Fine-tune classification head on custom context-distortion dataset.
- [ ] Task 1.3: Run baseline comparison (Similarity alone vs. NLI alone vs. Fused).
- [ ] Task 1.4: Output confusion matrix and classification report.

#### Member 2 (Data & Retrieval):
- [ ] Task 2.1: Expand `data/sample_pairs.json` to 200+ curated benchmark pairs.
- [ ] Task 2.2: Implement document window chunking (~80 words) in `retriever.py`.
- [ ] Task 2.3: Build FAISS index over article corpus and evaluate Recall@K.
- [ ] Task 2.4: Enhance regex & spaCy patterns for percentage/numerical shifts.

#### Member 3 (Backend & Systems - YOU):
- [x] Task 3.1: Initialize FastAPI app, routing, and CORS configuration.
- [x] Task 3.2: Implement model lazy-loading for instantaneous server boot.
- [x] Task 3.3: Build integrated fallback static UI (zero Node.js required).
- [ ] Task 3.4: Connect SQLite/PostgreSQL database to record every analysis.
- [ ] Task 3.5: Build `GET /api/history` endpoint with audit timestamps.
- [ ] Task 3.6: Verify Docker container build (`docker-compose up`).

#### Member 4 (Frontend):
- [ ] Task 4.1: Build React Claim/Source input forms with example loader.
- [ ] Task 4.2: Build dynamic Context Collapse Score progress bar.
- [ ] Task 4.3: Implement color-coded taxonomy badges (Exaggerated, Omitted, etc.).
- [ ] Task 4.4: Add drag-and-drop screenshot upload connected to `/api/analyze/image`.
- [ ] Task 4.5: Display past analysis history sidebar from `/api/history`.

---

## 4. Daily Standup Update Template

Every evening (e.g., by 8:00 PM), each member posts this 4-line update on the team's WhatsApp / Discord group:

```text
📅 Date: [DD/MM/YYYY]
👤 Member: [Your Name] (Role: [e.g., Member 3 - Backend])
✅ Completed Today: [What you built or tested today]
🔨 Working on Next: [What you plan to work on tomorrow]
⚠️ Blockers / Dependencies: [Any help needed from teammates, or 'None']
```

### Example:
```text
📅 Date: 29/09/2026
👤 Member: Raghav (Member 3 - Backend)
✅ Completed Today: Built FastAPI app, lazy-loaded DeBERTa model, all 10 tests passing
🔨 Working on Next: Hooking SQLite DB to save analysis history and creating GET /api/history
⚠️ Blockers / Dependencies: None. API is ready for Member 4 to test at http://127.0.0.1:8000/docs
```

---

## 5. Technical Architecture Contract (How Modules Communicate)

```text
       ┌───────────────────────────────┐
       │   Frontend (Member 4)         │
       └──────────────┬────────────────┘
                      │ HTTP POST /api/analyze/text
                      ▼
       ┌───────────────────────────────┐
       │   Backend (Member 3 - YOU)    │ ◄─── Saves to DB (history)
       └──────┬─────────────────┬──────┘
              │                 │
              ▼                 ▼
 ┌─────────────────────────┐  ┌─────────────────────────┐
 │ Data/Retrieval (M2)     │  │ ML / NLP (M1)           │
 │ - retriever.py (FAISS)  │  │ - semantic.py (DeBERTa) │
 │ - claim_extractor.py    │  │ - classifier.py (Fusion)│
 └─────────────────────────┘  └─────────────────────────┘
```

This clean architecture keeps everyone independent while building one cohesive, high-impact CSE minor project.
