from google.cloud import bigquery
from pprint import pprint


client = bigquery.Client()


def cleanup():
    datasets = client.list_datasets()

    # pprint(datasets)

    for dataset in datasets:
        tables = dataset.list_tables()

        pprint(tables)

        for table in tables:
            table.delete()

        dataset.delete()


    # bigquery_client.dataset('').delete()


def create_datasets():
    pass


def create_input_tables():
    pass


def create_output_table():
    pass











# print('Project:', bigquery_client.project)

# dataset_ids = [
#     'property_1',
#     'property_2',
# ]

# for dataset_id in dataset_ids:
#     bigquery_client.dataset(dataset_id).create()

# dataset = bigquery_client.dataset('my_new_dataset')

# query_results = bigquery_client.run_sync_query(
#     'SELECT * FROM `bigquery-public-data.noaa_gsod.gsod2015` LIMIT 10'
# )
#
#
# query_results.use_legacy_sql = False
#
# query_results.run()
#
# pprint(query_results.fetch_data())

# query_results = bigquery_client.run_sync_query(
#     'INSERT INTO `static-gravity-163312.my_new_dataset.my_new_table` (`schema_field`) VALUES ("Hello")'
# )


# query_results.use_legacy_sql = False
#
# query_results.run()
#
# pprint(query_results.fetch_data())
#

# table = dataset.table(
#     'my_new_table',
#     [bigquery.SchemaField('schema_field', 'STRING')],
# )
#
# table.create()

# tables = dataset.list_tables()

# for table in tables:
#     table.reload()
#
#     pprint(table.table_id)
#
#     mappings = table.insert_data([
#         ('Value'),
#         ('Another value'),
#         ('A third value'),
#     ])
#
#     pprint(mappings)

# pprint(dir(table))


def main():
    cleanup()

main()




