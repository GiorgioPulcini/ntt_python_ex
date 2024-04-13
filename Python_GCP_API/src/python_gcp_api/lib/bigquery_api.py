from google.cloud import bigquery
from google.api_core.exceptions import NotFound


class BigqueryApi:

    def __init__(self, project_id: str, dataset: str, table: str):
        self.project_id = project_id
        self.dataset = dataset
        self.table = table
        self.bq_client = bigquery.Client()

    def check_table(self) -> bool:
        try:
            self.bq_client.get_table(f"{self.project_id}.{self.dataset}.{self.table}")
            return True
        except NotFound:
            return False

    def execute_query(self, query: str):
        query_job = self.bq_client.query(query)
        results = query_job.result()
        return results

    def check_data(self) -> bool:
        query_check = f"SELECT COUNT(*) FROM {self.project_id}.{self.dataset}.{self.table}"
        query_result = list(self.execute_query(query_check))
        return query_result[0][0] > 0
