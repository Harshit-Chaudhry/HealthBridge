
FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .

# Install CPU-only PyTorch first
RUN pip install --no-cache-dir \
    torch \
    --index-url https://download.pytorch.org/whl/cpu

COPY src/ ./src/

# Install the application and its remaining dependencies
RUN pip install --no-cache-dir --no-deps . \
    && pip install --no-cache-dir \
       fastapi "uvicorn[standard]" qdrant-client \
       sentence-transformers google-genai

COPY data/ ./data/

CMD ["uvicorn", "main:app", "--app-dir", "src", "--host", "0.0.0.0", "--port", "8000"]
