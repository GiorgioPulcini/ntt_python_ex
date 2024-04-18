from google.cloud import storage
from google.api_core.exceptions import Forbidden, NotFound


class GCSApi:

    def __init__(self, project_id: str):
        self.project_id = project_id
        self.gcs_client = storage.Client()

    def check_bucket(self, bucket: str) -> bool:
        try:
            self.gcs_client.get_bucket(bucket)
            return True
        except Forbidden:
            return False

    def extract_query_from_bucket(self, bucket_name, file_name):
        bucket = self.gcs_client.bucket(bucket_name)
        try:
            query = bucket.blob(file_name)
            return query.download_as_text()
        except NotFound:
            return None
