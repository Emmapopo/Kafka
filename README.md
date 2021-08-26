### Documentation for Kafka Service

According to Kafka's offical website (https://kafka.apache.org/),

"""Apache Kafka is an open-source distributed event streaming platform used
by thousands of companies for high-performance data pipelines,
streaming analytics, data integration, and mission-critical applications."""

This application is a simple implementation of Kafka,

With the following specifications:
The Kafka Engine has 3 topics.

- The first topic has 1 partition
- The second topic has two partitions
- The third topic has three partitions

There are six major endpoints for this service. They include:

1. Add Producer: For adding a producer.

This is a POST Request
The path is - http://127.0.0.1:5000/kafka/producer/add
To register a new producer, you need supply:

a) the user_id - The only acceptable ID format is the UUID

NB: The request must be in form of JSON.

Here is a sample request:
{
"user_id": "180ef2a7-3274-4c70-8e39-5f1cd053f8b3"
}
Based on this request, there are three possible responses:

{"status": "Invalid uuid"}, 400 - for invalid uuid
{"status": f"{self.user_id} added"} - if successful
{"status": "user already added"} - if user is already registered
{"status": e} - where e represents any other error message


2. Add Consumer: For adding a consumer.

This is a POST Request
The path is - http://127.0.0.1:5000/kafka/consumer/add
To register a new producer, you need supply:

a) the consumer_id - The only acceptable ID format is the UUID
b) topic - the topic that the consumer wants to subscribe to.
(NB: There are only three topics - topic1, topic2, and topic3 - to choose from)

NB: The request must be in form of JSON.

Here is a sample request:
{
"consumer_id": "180ef2a7-3274-4c70-8e39-5f1cd053f8b3",
"topic": "3"
}
Based on this request, there are three possible responses:

{"status": "Invalid uuid"}, 400 - for invalid uuid
{"status": "topic is not valid"}, 400 - for invalid topic
{"status": f"{self.consumer_id} registered as consumer successfully"} - if successful
{"status": "consumer already added"} - if consumer is already registered
{"status": e} - where e represents any other error message

3. Login: For producers and consumers

This is a POST Request
The path is - http://127.0.0.1:5000/login/auth
To register a new producer, you need supply:

a) user_id - this is the id of the producer or consumer

The sample requestis of the JSON form:

{
"user_id": "f6400502-b088-4cca-b370-5b61d080a1d8"
}

Based on this request, here are the posible resposes:

If login is successful:
{
    "logged_in_as": [
        "producer"
    ],
    "login": true,
    "user_id": "f6400502-b088-4cca-b370-5b61d080a1d8"
}

If login is unssuccessful:
{
    "msg": "user not registered"
}

or 

{"status": e} - where e represents any other error message


