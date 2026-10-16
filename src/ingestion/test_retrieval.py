from sentence_transformers import SentenceTransformer

from ingestion.retriever import retrieve_chunks
from ingestion.vector_store import create_vector_store

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
client = create_vector_store()

query = "How can i prevent dengue ?"

results = retrieve_chunks(
    query = query,
    client = client,
    model = model,
    top_k = 4,
)

for result in results:
    print(
        f"\nDisease: {result['disease']}",
        f"\nSection: {result['section']}",
        f"\nScore: {result['score']}",
        f"\nText: {result['text']}"
    )