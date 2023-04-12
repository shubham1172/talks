import { DaprServer } from "@dapr/dapr";

const pubSubName = process.env.PUBSUB_NAME || "pubsub";
const topicName = process.env.TOPIC_NAME || "orders";

const serverPort = process.env.SERVER_PORT || 3000;

const daprServer = new DaprServer({ serverPort });
daprServer.pubsub.subscribe(pubSubName, topicName, (message) => {
    console.log(`Received message: ${JSON.stringify(message)}`);
});

await daprServer.start();