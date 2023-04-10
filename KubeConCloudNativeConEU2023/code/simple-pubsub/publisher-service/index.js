import { DaprClient } from '@dapr/dapr';

const pubSubName = "redis-pubsub";
const topicName = "orders";

const client = new DaprClient();

// start an infinite loop to publish messages
while (true) {
    // generate a random order!
    const orderId = Math.floor(Math.random() * 1000000);
    const order = {
        id: orderId,
        name: `Order ${orderId}`,
        amount: orderId * 100,
    }

    // publish a message
    await client.pubsub.publish(pubSubName, topicName, order);

    // log to stdout
    console.log(`Published order ${order.id}!`);

    // wait 5 seconds
    await new Promise(resolve => setTimeout(resolve, 5000));
}