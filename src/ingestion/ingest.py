from ingestion.loader import load_markdown_files
from ingestion.chunker import chunk_document
from ingestion.embedder import generate_embeddings
from ingestion.vector_store import (
    COLLECTION_NAME,
    create_vector_store,
    store_chunks,
)

def main():
    docs = load_markdown_files("/app/data/")

    chunks = [
        chunk 
        for doc in docs
        for chunk in chunk_document(doc)

    ]
    embedded_chunks= generate_embeddings(chunks)

    client = create_vector_store()

    try:
        store_chunks(client,embedded_chunks)
        count = client.count(
            collection_name = COLLECTION_NAME
        ).count

        print(f"Documents loaded {len(docs)}")
        print(f"Chunks generated {len(chunks)}")
        print(f"Vectors stored {count}")
    finally:
        client.close()

if __name__ == "__main__":
    main()
