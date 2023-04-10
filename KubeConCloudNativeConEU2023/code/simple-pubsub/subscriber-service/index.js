import { DaprServer } from "@dapr/dapr";

const pubSubName = "redis-pubsub";
const topicName = "orders";

const serverPort = process.env.SERVER_PORT || 3000;

const daprServer = new DaprServer({ serverPort });
daprServer.pubsub.subscribe(pubSubName, topicName, (message) => {
    console.log(`Received message: ${JSON.stringify(message)}`);
});

await daprServer.start();