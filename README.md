# LocalVector – Private On-Prem RAG for Sensitive Data

LocalVector is a **portable, privacy-first retrieval-augmented generation (RAG) pipeline** that runs entirely **on-premises or inside a customer’s private cloud**.  
It combines local embeddings, a high-performance vector store, and lightweight local LLM orchestration — with **zero data leakage**.

---

## Why LocalVector?

Modern enterprises want smart AI search and question-answering over their private data — **but can’t send sensitive documents to public clouds**.  
This creates a gap: businesses have knowledge trapped in contracts, policies, SLAs, legal docs, or customer records — but no safe way to unlock that with AI.

LocalVector solves this by providing a **self-contained RAG pipeline** that works **inside your secure environment**, so no sensitive data ever leaves your control.

---

## Key Use Cases

- **CRM & Enterprise SaaS**  
  Vendors (like Salesforce) whose clients demand AI-powered helpdesks, contract Q&A, or knowledge search — **without sending customer data to public APIs**.

- **Healthcare & Legal**  
  Hospitals, law firms, or compliance-heavy orgs needing LLM insights over private docs while staying **HIPAA**, **GDPR**, or **client-privilege** compliant.

- **Internal Helpdesks & Support**  
  Large companies needing an internal AI search assistant that can answer staff questions about policies, SLAs, or proprietary processes — **entirely on-prem**.

---

## How It Works

- **Split:** Documents are split into overlapping text chunks for semantic search.
- **Embed:** Chunks are embedded locally with `sentence-transformers` — no calls to external APIs.
- **Store:** Embeddings are indexed with `hnswlib` for fast approximate nearest neighbor search.
- **Retrieve:** Incoming queries are embedded locally, searched, and the best chunks are retrieved.
- **Orchestrate:** Retrieved context is combined into a prompt for a local LLM — ready to run with Ollama, LocalGPT, or your preferred on-prem model.

Everything stays inside **your private environment** — by design.

---

## Project Structure

```plaintext
.
├── data/
│   ├── raw/               # Source docs
│   ├── embeddings/        # Saved ANN index + chunk mapping
│
├── localvector/           # Core Python modules
│   ├── config.py
│   ├── splitter.py
│   ├── embedder.py
│   ├── vector_store.py
│   ├── llm_orchestrator.py
│
├── config.yaml            # Model + chunking config
├── requirements.txt       # Python dependencies
├── main.py                # CLI entry point
└── README.md
