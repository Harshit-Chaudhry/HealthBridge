from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

from ingestion.vector_store import COLLECTION_NAME


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def retrieve_chunks(
        query: str,
        client: QdrantClient,
        model: SentenceTransformer,
        top_k: int =4,
) -> list[dict]:
    query_vector = model.encode(
        query,
        normalize_embeddings=True,
    ).tolist()

    results = client.query_points(
        collection_name = COLLECTION_NAME,
        query=query_vector,
        limit=top_k,
        with_payload=True,

    ).points

    return [
        {
            **point.payload,
            "score": point.score,
        }
        for point in results
    ]