from google.cloud import pubsub_v1

project_id = "gcplayproject"
topic_id = "pythontopic"

publisher = pubsub_v1.PublisherClient()

topic_path = publisher.topic_path(project_id, topic_id)

for n in range(1, 10):
    data = "Message number {}".format(n)
    print(data)
    # Data must be a bytestring
    data = data.encode("utf-8")
    print(data)
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)
    print(future.result())

print(f"Published messages to {topic_path}.")
