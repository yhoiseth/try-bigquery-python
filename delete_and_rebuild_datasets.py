from google.cloud import bigquery
from pprint import pprint
import sys

project_name = sys.argv[1]
client = bigquery.Client(project_name)


def cleanup():
    datasets = client.list_datasets()

    for dataset in datasets:
        tables = dataset.list_tables()

        for table in tables:
            table.delete()

        dataset.delete()


def create_datasets():
    dataset_names = [
        'property_1',
        'property_2',
    ]

    for dataset_name in dataset_names:
        dataset = client.dataset(dataset_name)

        dataset.create()


def create_input_tables():
    table_names = [
        'day_1',
        'day_2',
    ]

    datasets = client.list_datasets()

    for dataset in datasets:
        for table_name in table_names:
            table = dataset.table(
                table_name,
                [bigquery.SchemaField('column_1', 'STRING')],
            )

            table.create()

            query_table_name = \
                dataset.dataset_id.replace(':', '.') + \
                '.' + \
                table_name

            values = '("A value"), ("A second value"), ("A third value")'

            query = client.run_sync_query(
                'INSERT INTO `%s` (`column_1`) VALUES %s' % (query_table_name, values)
            )

            query.use_legacy_sql = False

            query.run()



def create_output_table():
    pass


def main():
    cleanup()
    create_datasets()
    create_input_tables()
    create_output_table()

main()







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







