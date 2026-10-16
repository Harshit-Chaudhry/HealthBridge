import re

def chunk_document(document: dict) -> list[dict]:
    text = document["text"]
    sections = re.split(r"(?m)(?=^#{1,3}\s+)",text)

    chunks = []

    for section_text in sections:
        section_text = section_text.strip()

        if not section_text:
            continue

        heading_match = re.match(r"^#{1,3}\s+(.+)", section_text)
        heading = heading_match.group(1).strip() if heading_match else "Introduction"

        chunks.append({
            "disease": document["disease"],
            "source": document["source"],
            "section": heading,
            "text": section_text
        })

    return chunks