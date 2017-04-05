import datetime


def get_table_names(number_of_days):
    table_names = []

    today = datetime.date.today()

    for index in range(0, number_of_days):
        day = today - datetime.timedelta(index)

        table_names.append(
            'ga_sessions_' + day.strftime('%Y%m%d')
        )

    return table_names
