import datetime


def get_table_names(number_of_days):
    table_names = []

    today = datetime.date.today()

    for index in range(1, number_of_days + 1):
        day = today - datetime.timedelta(index)

        table_names.append(
            'ga_sessions_' + day.strftime('%Y%m%d')
        )

    return table_names
