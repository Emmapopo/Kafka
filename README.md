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

a) the producer_id - The only acceptable ID format is the UUID

NB: The request must be in form of JSON.

Here is a sample request:
{
"producer_id": "180ef2a7-3274-4c70-8e39-5f1cd053f8b3"
}
Based on this request, there are three possible responses:

{"status": "Invalid uuid"}, 400 - for invalid uuid
{"status": f"{self.producer_id} added"} - if successful
{"status": "producer already added"} - if producer is already registered
