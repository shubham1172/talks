DOCKER_REPOSITORY ?= ghcr.io/shubham1172/kubecon-demo
SIMPLE_PUBSUB_IMAGE_NAME ?= simple-pubsub
SIMPLE_PUBSUB_IMAGE_TAG ?= 0.1.0

.PHONY: create-docker-publisher
create-docker-publisher:
	docker buildx build --platform linux/amd64 --push \
		-t $(DOCKER_REPOSITORY)/$(SIMPLE_PUBSUB_IMAGE_NAME):$(SIMPLE_PUBSUB_IMAGE_TAG) \
		-f ./publisher-service/Dockerfile ./publisher-service

.PHONY: create-docker-subscriber
create-docker-subscriber:
	docker buildx build --platform linux/amd64 --push \
		-t $(DOCKER_REPOSITORY)/$(SIMPLE_PUBSUB_IMAGE_NAME):$(SIMPLE_PUBSUB_IMAGE_TAG) \
		-f ./subscriber-service/Dockerfile ./subscriber-service
