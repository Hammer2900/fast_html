import unittest
from time import time as timeobj

from fast_html import *


class PerformanceTesting(unittest.TestCase):
    def test_large_structure_generation_performance(self):
        num_divs = 100000
        start_time = timeobj()
        for _ in range(num_divs):
            ''.join(div('Content'))
        end_time = timeobj()
        execution_time = end_time - start_time
        max_execution_time = 0.130
        self.assertLessEqual(execution_time, max_execution_time)


class HtmlToStringTesting(unittest.TestCase):
    def test_html_converter(self):
        self.assertEqual(
            """root([div([p(['Some text'], )], _class="example")], )""",
            str(print_html_to_class('<div class="example"><p>Some text</p></div>')),
        )


if __name__ == '__main__':
    unittest.main()
