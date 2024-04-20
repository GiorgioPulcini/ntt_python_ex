import unittest
from dotenv import load_dotenv
from python_gcp_api.lib.bigquery_api import BigqueryApi


class BigqueryApiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()

    def test_check_table_true(self):
        # Given
        given_project_id = "training-gcp-309207"
        given_dataset = "ex_pulcinig"
        given_table = "eu_country_summary"
        # When
        bq_api = BigqueryApi(given_project_id)
        # Then
        self.assertTrue(bq_api.check_table(given_dataset, given_table))

    def test_check_table_false(self):
        # Given
        given_project_id = "training-gcp-309207"
        given_dataset = "ex_pulcinig"
        given_table = "not_a_table"
        # When
        bq_api = BigqueryApi(given_project_id)
        # Then
        self.assertFalse(bq_api.check_table(given_dataset, given_table))

    def test_check_data_true(self):
        # Given
        given_project_id = "training-gcp-309207"
        given_dataset = "ex_pulcinig"
        given_table = "eu_country_summary"
        # When
        bq_api = BigqueryApi(given_project_id)
        # Then
        self.assertTrue(bq_api.check_data(given_dataset, given_table))

    def test_check_data_false(self):
        # Given
        given_project_id = "training-gcp-309207"
        given_dataset = "ex_pulcinig"
        given_table = "empty_table"
        # When
        bq_api = BigqueryApi(given_project_id)
        # Then
        self.assertFalse(bq_api.check_data(given_dataset, given_table))

    def test_execute_query_ok(self):
        # Given
        given_project_id = "training-gcp-309207"
        given_dataset = "ex_pulcinig"
        given_table = "eu_country_summary"
        given_query_test = f"SELECT country_name " \
                           f"FROM {given_project_id}.{given_dataset}.{given_table} " \
                           f"WHERE UPPER(TRIM(capital_city)) = 'LISBON' "
        given_results = "Portugal"
        # When
        bq_api = BigqueryApi(given_project_id)
        query_result = bq_api.execute_query(given_query_test)
        # Then
        self.assertEqual(given_results, list(query_result)[0][0])

    def test_execute_query_not_ok(self):
        # Given
        given_project_id = "training-gcp-309207"
        given_dataset = "ex_pulcinig"
        given_table = "eu_country_summary"
        given_query_test = f"SELECT country_name " \
                           f"FROM {given_project_id}.{given_dataset}.{given_table} " \
                           f"WHERE UPPER(TRIM(capital_city)) = 'LISBON' "
        given_results = "France"
        # When
        bq_api = BigqueryApi(given_project_id)
        query_result = bq_api.execute_query(given_query_test)
        # Then
        self.assertNotEqual(given_results, list(query_result)[0][0])


if __name__ == '__main__':
    unittest.main()
