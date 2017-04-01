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


def create_input_datasets():
    dataset_names = [
        'property_1',
        'property_2',
    ]

    for dataset_name in dataset_names:
        create_dataset(dataset_name)


def create_dataset(name):
    dataset = client.dataset(name)
    dataset.create()


def create_and_populate_input_tables():
    table_names = [
        'day_1',
        'day_2',
    ]

    datasets = client.list_datasets()

    for dataset in datasets:
        for table_name in table_names:
            create_table(dataset, table_name, [bigquery.SchemaField('column_1', 'STRING')])

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


def create_table(dataset, name, schema_fields):
    table = dataset.table(name, schema_fields)
    table.create()


def create_output_dataset():
    create_dataset('output')


def create_output_table():
    dataset = client.dataset('output')

    schema_fields = [
        bigquery.SchemaField('column_1', 'STRING'),
        bigquery.SchemaField('country_code', 'STRING'),
        bigquery.SchemaField('property_id', 'STRING'),
        bigquery.SchemaField('property_name', 'STRING'),
    ]

    create_table(dataset, 'output_table', schema_fields)


def main():
    cleanup()
    create_input_datasets()
    create_and_populate_input_tables()
    create_output_dataset()
    create_output_table()

main()
