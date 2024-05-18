import unittest
from unittest.mock import patch
from google.cloud import bigquery
from python_gcp_api.lib.bigquery_api import BigqueryApi


class BigqueryApiTest(unittest.TestCase):

    @patch('google.cloud.bigquery.Client')
    def test_check_table_true(self, mock_client):
        mock_client.return_value.get_table.return_value = True
        given_project_id = "training"
        given_dataset = "ex_pulcinig"
        given_table = "eu_country_summary"
        bq_api = BigqueryApi()
        # Then
        self.assertTrue(bq_api.check_table(given_project_id, given_dataset, given_table))

    @patch('google.cloud.bigquery.Client')
    def test_check_table_false(self, mock_client):
        mock_client.return_value.check_table.return_value = False
        given_project_id = "training"
        given_dataset = "ex_pulcinig"
        given_table = "eu_country_summary"
        bq_api = BigqueryApi()
        self.assertTrue(bq_api.check_table(given_project_id, given_dataset, given_table))

    @patch('google.cloud.bigquery.Client')
    def test_check_data_true(self, mock_client):
        mock_client.return_value.query.return_value.result.return_value = iter([bigquery.Row((1,), {"count": 0})])
        given_project_id = "training"
        given_dataset = "ex_pulcinig"
        given_table = "eu_country_summary"
        bq_api = BigqueryApi()
        self.assertTrue(bq_api.check_data(given_project_id, given_dataset, given_table))

    @patch('google.cloud.bigquery.Client')
    def test_check_data_false(self, mock_client):
        mock_client.return_value.query.return_value.result.return_value = iter([bigquery.Row((0,), {"count": 0})])
        given_project_id = "training"
        given_dataset = "ex_pulcinig"
        given_table = "eu_country_summary"
        bq_api = BigqueryApi()
        self.assertFalse(bq_api.check_data(given_project_id, given_dataset, given_table))

    @patch('google.cloud.bigquery.Client')
    def test_execute_query_ok(self, mock_client):
        mock_client.return_value.query.return_value.result.return_value = iter([bigquery.Row(("value1", "value2"), {"col1": 0, "col2": 1})])
        bq_api = BigqueryApi()
        query_result = bq_api.execute_query("SELECT * FROM `table`")
        result_list = list(query_result)[0]
        self.assertEqual(result_list[0], "value1")
        self.assertEqual(result_list[1], "value2")


if __name__ == '__main__':
    unittest.main()
