# Simple Pub/Sub Sample using JS-SDK

This sample demonstrates how to use Dapr's JS-SDK to publish and subscribe to messages. Here we have a simple publisher and subscriber. The publisher publishes a message to a topic, and the subscriber receives the message and prints it out. The setup runs on Kubernetes.

## Prerequisites

1. CLI tools: [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/), [helm](https://helm.sh/docs/intro/install/), [dapr](https://docs.dapr.io/getting-started/install-dapr-cli/), [kubetail](https://github.com/johanhaleby/kubetail)

2. Install Dapr on your Kubernetes cluster. 
```bash
dapr init -k
```

3. Install Redis and Kafka on your Kubernetes cluster. 
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install redis bitnami/redis --set image.tag=6.2
helm install kafka bitnami/kafka --set image.tag=3.4.0
```

## Running the sample

Deploy
```bash
kubectl apply -f deploy/redis-pubsub.yaml
kubectl apply -f deploy/subscriber-service.yaml
kubectl apply -f deploy/publisher-service.yaml
```

See the logs
```bash
kubetail subscriberapp -c subscriber
kubetail publisherapp -c publisher
```

Scaling the subscriber
```bash
kubectl scale deployment subscriberapp --replicas=3
```

Adding an additional subscriber
```bash
kubectl apply -f deploy/subscriber-service-2.yaml
kubetail subscriberapp-2 -c subscriber
```

Swapping component
```bash
kubectl apply -f deploy/kafka-pubsub.yaml
kubectl set env deployment publisherapp PUBSUB_NAME=kafka-pubsub
kubectl set env deployment subscriberapp PUBSUB_NAME=kafka-pubsub
```

Clean up
```bash
kubectl delete -f ./deploy --ignore-not-found=true
```
