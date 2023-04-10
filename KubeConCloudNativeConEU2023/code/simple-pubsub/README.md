# Demo #1

This sample demonstrates how to use the Pub/Sub API to publish and subscribe to messages.
Here we have a simple publisher and subscriber. The publisher publishes a message to a topic, and the subscriber receives the message and prints it out. They run as Kubernetes pods.


## Prerequisites

1. CLI tools: [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/), [helm](https://helm.sh/docs/intro/install/), [dapr](https://docs.dapr.io/getting-started/install-dapr-cli/)

2. Install Dapr on your Kubernetes cluster. 
```bash
dapr init -k
```

3. Install Redis on your Kubernetes cluster. 
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install redis bitnami/redis --set image.tag=6.2
```

## Running the sample

```bash
# Add the Redis component
kubectl apply -f ./deploy/redis-pubsub.yaml
# Add the publisher-service 
kubectl apply -f ./deploy/publisher-service.yaml
# Add the subscriber-service
kubectl apply -f ./deploy/subscriber-service.yaml
```
