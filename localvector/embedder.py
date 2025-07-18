from sentence_transformers import SentenceTransformer

class LocalEmbedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_chunks(self, chunks):
        return self.model.encode(chunks, show_progress_bar=True)

    def embed_query(self, query):
        return self.model.encode([query])[0]
