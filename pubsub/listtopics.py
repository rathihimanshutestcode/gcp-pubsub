from google.cloud import pubsub_v1

# TODO(developer)
project_id = "gcplayproject"

publisher = pubsub_v1.PublisherClient()
project_path = f"projects/{project_id}"

for topic in publisher.list_topics(request={"project": project_path}):
    print(topic)
