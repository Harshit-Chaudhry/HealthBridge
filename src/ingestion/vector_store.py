from qdrant_client import QdrantClient, models

COLLECTION_NAME = "healthbridge_diseases"
VECTOR_SIZE = 384

STORAGE_PATH = "/app/qdrant_data"

def create_vector_store():
    client = QdrantClient(path=STORAGE_PATH)

    if not client.collection_exists(COLLECTION_NAME):

        client.create_collection(
            collection_name = COLLECTION_NAME,
            vectors_config = models.VectorParams(
                size = VECTOR_SIZE,
                distance = models.Distance.COSINE,
            ),
        )

    return client

def store_chunks(client, chunks: list[dict]) -> None :
    points = []
    for idx,chunk in enumerate(chunks):
        points.append(
            models.PointStruct(
                id = idx,
                vector=chunk["embedding"],
                payload = {
                    "disease": chunk["disease"],
                    "source": chunk["source"],
                    "section": chunk["section"],
                    "text": chunk["text"],
                },
            )
        )
    client.upsert(
        collection_name = COLLECTION_NAME,
        points=points,
    )