from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError


class PubSubApi:

    def __init__(self):
        self.pub_client = pubsub_v1.PublisherClient()
        self.sub_client = pubsub_v1.SubscriberClient()

    def publish_message(self, project_id, topic_id, message):
        topic_path = self.pub_client.topic_path(project_id, topic_id)
        message_in_bytes = message.encode("utf-8")
        self.pub_client.publish(topic_path, message_in_bytes)

    @staticmethod
    def message_callback(message):
        print(f"Message Received: {message.data.decode('utf-8')}")
        message.ack()

    def receive_messages(self, project_id, subscription_id, callback, timeout):
        subscription_path = self.sub_client.subscription_path(project_id, subscription_id)
        listener = self.sub_client.subscribe(subscription_path, callback=callback)
        try:
            listener.result(timeout=timeout)
        except TimeoutError:
            listener.cancel()
