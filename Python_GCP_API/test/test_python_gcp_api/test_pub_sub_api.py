import unittest
from unittest.mock import patch
from python_gcp_api.lib.pub_sub_api import PubSubApi


class PubSubApiTest(unittest.TestCase):

    @patch('google.cloud.pubsub_v1.PublisherClient')
    @patch('google.cloud.pubsub_v1.SubscriberClient')
    def test_publish_message(self, mock_sub_client, mock_pub_client):
        mock_sub_client.return_value = True
        mock_pub_client.return_value.topick_path.return_value = "topic_path"
        mock_pub_client.return_value.publish.return_value = True
        given_project_id = "training"
        given_topic_id = "ex_pulcinig"
        given_message = "test"
        pubsub_api = PubSubApi()
        self.assertTrue(pubsub_api.publish_message(given_project_id, given_topic_id, given_message))