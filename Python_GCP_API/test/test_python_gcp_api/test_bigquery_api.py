import unittest
from dotenv import load_dotenv
from python_gcp_api.bigquery_api import BigqueryApi


class BigqueryApiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()

    def test_check_table_true(self):
        # Given
        given_project_id = "training-gcp-309207"
        given_dataset = "excellenceacademycarlolombardi"
        given_table = "studente_table"
        # When
        bq_api = BigqueryApi(given_project_id, given_dataset, given_table)
        # Then
        self.assertTrue(bq_api.check_table())

    def test_check_table_false(self):
        # Given
        given_project_id = "training-gcp-309207"
        given_dataset = "excellenceacademycarlolombardi"
        given_table = "fake_tables"
        # When
        bq_api = BigqueryApi(given_project_id, given_dataset, given_table)
        # Then
        self.assertFalse(bq_api.check_table())


if __name__ == '__main__':
    unittest.main()
