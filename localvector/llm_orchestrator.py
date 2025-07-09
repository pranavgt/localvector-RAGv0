class LocalLLM:
    def generate(self, query, context_chunks):
        prompt = f"Answer the question: '{query}'\n\nContext:\n"
        for chunk in context_chunks:
            prompt += f"- {chunk}\n"
        return f"[LLM Placeholder] {prompt}"
