# LocalVector – Project Structure

A portable, privacy-first RAG (Retrieval-Augmented Generation) pipeline that runs entirely on-prem or inside a customer’s private cloud.

---

## Folders

```plaintext
.
├── data/
│   ├── raw/               # Original source docs, e.g. sample.txt
│   ├── embeddings/        # Saved ANN index + chunk text mapping
│
├── localvector/           # Core Python package
│   ├── __init__.py
│   ├── config.py          # Loads settings from config.yaml
│   ├── splitter.py        # Splits documents into overlapping text chunks
│   ├── embedder.py        # Creates local embeddings (SentenceTransformers)
│   ├── vector_store.py    # ANN search index (HNSWlib), chunk mapping
│   ├── llm_orchestrator.py # Builds final prompt with retrieved context
│
├── config.yaml            # Model, chunking, and index config
├── requirements.txt       # Python dependencies
├── main.py                # CLI entry point: run queries from terminal
├── README.md              # Project overview & usage
└── project_structure.md   # This file
```
## Key Files

### `data/raw/sample.txt`
Your input document(s). Use realistic internal text for testing.

### `localvector/config.py`
Loads `config.yaml` for:
- Embedding model name
- Chunk size & overlap
- ANN index path

### `localvector/splitter.py`
Splits large docs into smaller overlapping chunks for better retrieval.

### `localvector/embedder.py`
Runs local embeddings using `sentence-transformers`. No cloud calls.

### `localvector/vector_store.py`
- Stores embeddings in an ANN index (`hnswlib`).
- Keeps a `chunk_texts` list to map vector IDs back to source text.
- Saves both the index and `.chunks` file to disk.

### `localvector/llm_orchestrator.py`
Combines the question plus retrieved chunks into a prompt.  
Currently uses a placeholder — ready to be swapped for a real local LLM (Ollama, LocalGPT, transformers).

### `main.py`
Command line runner:
```bash
python main.py "Your question here"
