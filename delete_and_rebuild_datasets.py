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

            values = [
                '("A value from %s.%s")' % (dataset.name, table_name),
                '("A second value from %s.%s")' % (dataset.name, table_name),
                '("A third value from %s.%s")' % (dataset.name, table_name),
            ]

            query = 'INSERT INTO `%s` (`column_1`) VALUES %s' % (query_table_name, ', '.join(values))

            run_query(query)


def run_query(query):
    query_results = client.run_sync_query(query)
    query_results.use_legacy_sql = False
    query_results.run()


def create_table(dataset, name, schema_fields):
    table = dataset.table(name, schema_fields)
    table.create()


def create_output_dataset():
    create_dataset('output')


def create_output_table():
    dataset = client.dataset('output')

    schema_fields = [
        bigquery.SchemaField('column_1', 'STRING'),
        bigquery.SchemaField('property_id', 'STRING'),
        bigquery.SchemaField('property_name', 'STRING'),
        bigquery.SchemaField('country_code', 'STRING'),
    ]

    create_table(dataset, 'output_table', schema_fields)


def populate_output_table():
    properties = get_properties()

    for property in properties:
        dataset = client.dataset(property['name'])

        tables = dataset.list_tables()

        for table in tables:
            query_parts = [
                'INSERT INTO `%s.output.output_table`' % (project_name),
                '(column_1, property_id, property_name, country_code)',
                'SELECT column_1, "%s", "%s", "%s"' % (
                    property['id'],
                    property['name'],
                    property['country_code']
                ),
                'FROM `%s.%s.%s`' % (project_name, dataset.name, table.name),
            ]

            query = ' '.join(query_parts)

            run_query(query)


def get_properties():
    return [
        {
            'id': '1',
            'name': 'property_1',
            'country_code': 'uk',
        },
        {
            'id': '2',
            'name': 'property_2',
            'country_code': 'nz'
        },
    ]


def main():
    cleanup()
    create_input_datasets()
    create_and_populate_input_tables()
    create_output_dataset()
    create_output_table()
    populate_output_table()

main()
