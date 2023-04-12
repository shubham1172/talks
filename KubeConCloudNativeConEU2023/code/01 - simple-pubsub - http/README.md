# Simple Pub/Sub Sample using HTTP APIs

This sample demonstrates how to use the Pub/Sub HTTP APIs to publish and subscribe to messages. This uses the Dapr's self-hosted mode to run locally on your machine.

## Prerequisites

1. [Install Dapr CLI](https://docs.dapr.io/getting-started/install-dapr-cli/)

2. Install Dapr on your local machine.
```bash
dapr init
```

## Publishing messages

1. Run a daprd process for publishing messages.
```bash
dapr run --app-id publisher-app --dapr-http-port 3500 -- sleep 1000
```

2. Use publish.http to publish messages to a topic.

3. Use a Redis client to validate (e.g. Redis CLI or Medis)

## Subscribing to messages

1. Run the subscriber application
```bash
dapr run --app-id subscriber-app --app-protocol http --app-port 3000 -- python3 subscriber.py
```

