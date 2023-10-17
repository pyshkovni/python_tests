# Тестируем bubble_sort

import unittest
from handlers import bubble_sort


class BubbleSortTest(unittest.TestCase):
    # нужно указать наследование от суб-класса TestCase

    # проверяющие методы должны начинаться с test_
    def test_normal(self):
        # запускаем тестируемую функцию
        result = bubble_sort([3, 4, 2, 8, 1, 6, 4])
        # проверяем что она вернула
        self.assertEqual(result, [1, 2, 3, 4, 4, 6, 8])

    # в именах методов-проверок очень желательно указывать
    # какой вариант они проверяют
    def test_sorted(self):
        result = bubble_sort([3, 4, 5])
        # так же можно писать детализирующее сообщение
        self.assertEqual(result, [3, 4, 5], 'не работает сортировка отсортированного списка')

    # и так далее - записываем все возможные случаи
    def test_reversed(self):
        result = bubble_sort([3, 2, 1])
        self.assertEqual(result, [1, 2, 3])

    def test_empty(self):
        result = bubble_sort([])
        self.assertEqual(result, [])

    def test_with_negative(self):
        result = bubble_sort([9, 3, -7, 2])
        self.assertEqual(result, [-7, 2, 3, 9])


if __name__ == "__main__":
    # запуск автодискавера тестов
    unittest.main()

    # Если тест провален, то будет сообщение об ошибке
    # если метод называется с test_, то класс понимает, что их надо вызвать
    # методы без test_ автоматически не вызываются.
    # Таким образом можно автоматизировать проверки написанного кода.
    # И в промышленном программировании тесты неотъемлемая часть программного продукта.
