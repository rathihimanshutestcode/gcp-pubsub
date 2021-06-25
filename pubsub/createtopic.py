from google.cloud import pubsub_v1


project_id = "gcplayproject"
topic_id = "pythontopic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

topic = publisher.create_topic(request={"name": topic_path})

print("Created topic: {}".format(topic.name))
