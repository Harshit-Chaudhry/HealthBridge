from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def generate_embeddings(chunks: list[dict]) -> list[dict]:
    model = SentenceTransformer(MODEL_NAME)

    texts = [chunk["text"] for chunk in chunks]

    vectors = model.encode(
        texts,
        normalize_embeddings = True,
        show_progress_bar=True,

    )

    embedded_chunks = []

    for chunk, vector in zip(chunks, vectors):
        embedded_chunks.append({
            **chunk,
            "embedding": vector.tolist(),
        })

    return embedded_chunks