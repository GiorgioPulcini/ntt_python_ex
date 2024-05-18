import unittest
from unittest.mock import patch
from google.cloud import storage
from python_gcp_api.lib.gcs_api import GCSApi


class GCSApiTest(unittest.TestCase):

    @patch('google.cloud.storage.Client')
    def test_check_bucket_true(self, mock_client):
        mock_client.return_value.get_bucket.return_value = True
        given_bucket = "ex_pulcinig"
        gcs_api = GCSApi()
        # Then
        self.assertTrue(gcs_api.check_bucket(given_bucket))

    @patch('google.cloud.storage.Client')
    def test_check_bucket_false(self, mock_client):
        mock_client.return_value.get_bucket.return_value = False
        given_bucket = "ex_pulcinig"
        gcs_api = GCSApi()
        # Then
        self.assertFalse(gcs_api.check_bucket(given_bucket))

    @patch('google.cloud.storage.Client')
    def test_extract_query(self, mock_client):
        mock_client.return_value.bucket.return_value.blob.return_value.download_as_text.return_value = "text"
        given_bucket = "ex_pulcinig"
        given_file = "query.txt"
        gcs_api = GCSApi()
        query_extract = gcs_api.extract_query_from_bucket(given_bucket, given_file)
        # Then
        self.assertTrue(len(query_extract) > 0)


if __name__ == '__main__':
    unittest.main()
