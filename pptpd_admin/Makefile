.PHONY: dev

run:
	uvicorn main:app --reload --host 0.0.0.0 --port 8000 --workers 2

dev:
	docker build -f build.Dockerfile . -t $(tag)

stage:
	docker build . -t $(tag)
