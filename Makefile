.PHONY: build
build:
	DOCKER_BUILDKIT=1 docker build --file Dockerfile --tag localnoetl/noetl-plugin-http-handler:v0.0.1 ./
