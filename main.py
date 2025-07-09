import sys
from localvector.config import load_config
from localvector.splitter import split_document
from localvector.embedder import LocalEmbedder
from localvector.vector_store import VectorStore
from localvector.llm_orchestrator import LocalLLM

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your question here\"")
        sys.exit(1)

    query = sys.argv[1]
    config = load_config()
    embedder = LocalEmbedder(config["embedding_model"])
    store = VectorStore()

    try:
        store.load_index(config["vector_store_path"])
        print("Loaded existing index.")
    except FileNotFoundError:
        print("No existing index, creating a new one.")
        with open("data/raw/sample.txt") as f:
            text = f.read()
        chunks = split_document(text, config["chunk_size"], config["chunk_overlap"])
        print(f"Chunks created: {len(chunks)}")
        embeddings = embedder.embed_chunks(chunks)
        store.add_embeddings(embeddings, chunks)
        store.save_index(config["vector_store_path"])
        print("Index saved.")

    query_emb = embedder.embed_query(query)
    results, distances = store.search(query_emb, top_k=3)

    print("\n=== Retrieved Chunks ===")
    for i, chunk in enumerate(results):
        print(f"Chunk {i+1}: {chunk[:100]}...")
        print(f"Distance: {distances[i]:.4f}")

    llm = LocalLLM()
    answer = llm.generate(query, context_chunks=results)
    print("\n=== Final Answer ===")
    print(answer)

if __name__ == "__main__":
    main()
