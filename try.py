from google.cloud import bigquery
from pprint import pprint

bigquery_client = bigquery.Client()

projects = bigquery_client.list_projects()

print('Project:', bigquery_client.project)


