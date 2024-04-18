import unittest
from dotenv import load_dotenv
from python_gcp_api.lib.gcs_api import GCSApi


class GCSApiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()

    def test_check_bucket_true(self):
        # Given
        given_project_id = "training-gcp-309207"
        given_bucket = "ex_pulcinig"
        # When
        gcs_api = GCSApi(given_project_id)
        # Then
        self.assertTrue(gcs_api.check_bucket(given_bucket))

    def test_check_bucket_false(self):
        # Given
        given_project_id = "training-gcp-309207"
        given_bucket = "fake_bucket"
        # When
        gcs_api = GCSApi(given_project_id)
        # Then
        self.assertFalse(gcs_api.check_bucket(given_bucket))

    def test_extract_query_ok(self):
        # Given
        given_project_id = "training-gcp-309207"
        given_bucket = "ex_pulcinig"
        given_file = "query.txt"
        # When
        gcs_api = GCSApi(given_project_id)
        query_extract = gcs_api.extract_query_from_bucket(given_bucket, given_file)
        # Then
        self.assertTrue(len(query_extract) > 0)

    def test_extract_query_not_ok(self):
        # Given
        given_project_id = "training-gcp-309207"
        given_bucket = "ex_pulcinig"
        given_file = "not_real_file.txt"
        # When
        gcs_api = GCSApi(given_project_id)
        query_extract = gcs_api.extract_query_from_bucket(given_bucket, given_file)
        # Then
        self.assertIsNone(query_extract)


if __name__ == '__main__':
    unittest.main()
