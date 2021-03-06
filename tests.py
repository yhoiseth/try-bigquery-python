import unittest
from datetime import date
from datetime import timedelta
import tableutilities


class TestTableUtilities(unittest.TestCase):
    def test_get_table_names(self):
        today = date.today()
        one_day = timedelta(1)
        yesterday = today - one_day
        two_days_ago = yesterday - one_day
        three_days_ago = two_days_ago - one_day

        date_format = '%Y%m%d'

        prefix = 'ga_sessions_'

        expected_table_names = [
            prefix + yesterday.strftime(date_format),
            prefix + two_days_ago.strftime(date_format),
            prefix + three_days_ago.strftime(date_format),
        ]

        actual_table_names = tableutilities.get_table_names(3)

        self.assertEqual(3, len(actual_table_names))
        self.assertEqual(
            expected_table_names, actual_table_names
        )

if __name__ == '__main__':
    unittest.main()
