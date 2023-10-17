# С помощью Python можно делать имитации для кода.
# Программист может зафиксировать поведение внешних источников данных.

# Для упрощения этого процесса есть библиотека - unittest.mock
# Которая позволяет делать mock-объекты (пустышки)


import unittest
from unittest.mock import Mock
from collections.abc import Iterable

import handlers
from handlers import ExternalResourceGetter

_test_html = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


class ExternalResourceGetterTest(unittest.TestCase):

    def test_normal(self):
        getter = ExternalResourceGetter(url='some-url')
        fake_result = Mock()
        fake_result.text = _test_html
        fake_get_result = Mock(return_value=fake_result)
        handlers.requests.get = fake_get_result
        result = getter.run()
        self.assertEqual(isinstance(result, Iterable), True)


if __name__ == '__main__':
    unittest.main()
