import os
from python_gcp_api.lib.bigquery_api import BigqueryApi
from python_gcp_api.lib.gcs_api import GCSApi
from python_gcp_api.utils.set_google_credentials import set_google_credentials
from google.api_core.exceptions import BadRequest

# input parameters
project_id = "training-gcp-309207"
input_dataset = "ex_pulcinig"
input_table = "eu_country_summary"
input_bucket = "ex_pulcinig"
input_file = "query.txt"

cd = os.getcwd()
output_file_name = "result"
output_result_path = cd + "/results/"
if os.path.exists(output_result_path):
    pass
else:
    os.mkdir(output_result_path)

credential_path = "path\\to\\your\\google\\credentials.json"

# set google credentials for service account
set_google_credentials(credential_path)
# initialize Bigquery and GCS client
try:
    bq_client = BigqueryApi(project_id)
    gcs_client = GCSApi(project_id)
    # verify table existence
    if bq_client.check_table(input_dataset, input_table) and bq_client.check_data(input_dataset, input_table):
        # verify bucket existence
        if gcs_client.check_bucket(input_bucket):
            # extract query
            query = gcs_client.extract_query_from_bucket(input_bucket, input_file)
            # execute query
            if query is not None:
                result = bq_client.execute_query(query)
                # save result to a csv
                df = result.to_dataframe()
                print(df)
                df.to_csv(f"{output_result_path}{output_file_name}.csv")
            else:
                print("Error: query file doesn't exist")
        else:
            print("Error: bucket doesn't exist or access on it is denied")
    else:
        print("Error: table doesn't exist or table is empty")
except BadRequest:
    print("Sorry, project doesn't exist or access on it is denied")
