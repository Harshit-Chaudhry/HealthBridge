from pathlib import Path

def load_markdown_files(data_dir: str = "data") -> list[dict]:
    data_path = Path(data_dir)
    documents = []

    for file_path in data_path.glob("*.md"):
        text = file_path.read_text(encoding="utf-8").strip()

        if not text:
            continue 

        documents.append({
            "disease": file_path.stem,
            "source": file_path.name,
            "text": text,
        })
    return documents