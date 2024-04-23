import os, logging, sys
from python_gcp_api.lib.bigquery_api import BigqueryApi
from python_gcp_api.lib.gcs_api import GCSApi
from python_gcp_api.utils.set_google_credentials import set_google_credentials
from google.api_core.exceptions import BadRequest


# initialize logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
LOGGER = logging.getLogger(__name__)

# input parameters
project_id = "training-gcp-309207"
input_dataset = "ex_pulcinig"
input_table = "eu_country_summary"
input_bucket = "ex_pulcinig"
input_file = "query.txt"

# output parameters
cd = os.getcwd()
output_file_name = "result"
output_result_path = cd + "/results/"
if os.path.exists(output_result_path):
    pass
else:
    os.mkdir(output_result_path)

# set google credentials for service account
credential_path = "path\\to\\your\\google\\credentials.json"
try:
    set_google_credentials(credential_path)
    LOGGER.info("Google Credentials set correctly!")
except FileNotFoundError:
    LOGGER.error("Sorry! Credentials file doesn't exist, please check the path")
    exit(1)

# initialize Bigquery and GCS client
LOGGER.info("Initializing Client...")
try:
    bq_client = BigqueryApi(project_id)
    gcs_client = GCSApi(project_id)
    # verify table existence
    LOGGER.info("Checking bq table...")
    if bq_client.check_table(input_dataset, input_table) and bq_client.check_data(input_dataset, input_table):
        # verify bucket existence
        LOGGER.info("Checking gcs bucket...")
        if gcs_client.check_bucket(input_bucket):
            # extract query
            LOGGER.info("Extracting query...")
            query = gcs_client.extract_query_from_bucket(input_bucket, input_file)
            # execute query
            if query is None:
                LOGGER.error("Query file doesn't exist")
            else:
                LOGGER.info("Executing query...")
                result = bq_client.execute_query(query)
                LOGGER.info("Saving result...")
                # save result to a csv
                df = result.to_dataframe()
                print(df)
                df.to_csv(f"{output_result_path}{output_file_name}.csv")
                LOGGER.info(f"Data correctly saved on {output_result_path}{output_file_name}.csv")
        else:
            LOGGER.error("Bucket doesn't exist or access on it is denied")
    else:
        LOGGER.error("Table doesn't exist or it's empty, or you do not have access on it")
except BadRequest:
    LOGGER.error("Sorry, project doesn't exist or access on it is denied")
