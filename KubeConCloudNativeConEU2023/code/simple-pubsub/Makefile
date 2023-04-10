DOCKER_REPOSITORY ?= ghcr.io/shubham1172/kubecon-demo
SIMPLE_PUBSUB_IMAGE_NAME ?= simple-pubsub
SIMPLE_PUBSUB_IMAGE_TAG ?= 0.1.0

.PHONY: build-docker-publisher
build-docker-publisher:
	docker build -t $(DOCKER_REPOSITORY)/$(SIMPLE_PUBSUB_IMAGE_NAME):$(SIMPLE_PUBSUB_IMAGE_TAG) -f ./publisher-service/Dockerfile ./publisher-service

.PHONY: push-docker-publisher
push-docker-publisher:
	docker push $(DOCKER_REPOSITORY)/$(SIMPLE_PUBSUB_IMAGE_NAME):$(SIMPLE_PUBSUB_IMAGE_TAG)

.PHONY: build-docker-subscriber
build-docker-subscriber:
	docker build -t $(DOCKER_REPOSITORY)/$(SIMPLE_PUBSUB_IMAGE_NAME):$(SIMPLE_PUBSUB_IMAGE_TAG) -f ./subscriber-service/Dockerfile ./subscriber-service

.PHONY: push-docker-subscriber
push-docker-subscriber:
	docker push $(DOCKER_REPOSITORY)/$(SIMPLE_PUBSUB_IMAGE_NAME):$(SIMPLE_PUBSUB_IMAGE_TAG)