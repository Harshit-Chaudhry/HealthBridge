
.PHONY: test-retrieval logs shell health

ingest:
	docker exec -w /app/src healthbridge python -m ingestion.ingest

test-retrieval:
	docker exec -w /app/src healthbridge python -m ingestion.test_retrieval

logs:
	docker logs -f healthbridge

shell:
	docker exec -it healthbridge bash

health:
	curl -s http://localhost:8000/health
