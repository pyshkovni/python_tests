# Модуль с функциями

# импорты
import time
import sys
import requests  # pip install requests

sys.set_int_max_str_digits(0)


'''Some handlers to do stuff'''


def get_time_track(precision: int):
    """
    The function accepts the accuracy and returns the running time of the calculation

    :param precision:
    :return:
    """
    def time_track(func):
        def wrapper(*args, **kwargs):
            started_at = time.monotonic()
            result = func(*args, **kwargs)
            ended_at = time.monotonic()
            elapsed = round(ended_at - started_at, precision)
            print(f'Функция работала {elapsed} секунд(ы)')
            return result
        return wrapper
    return time_track


def bubble_sort(arr: list):
    """
    Bubble sorting compares two adjacent elements.
    If the adjacent elements are in the wrong position, a replacement will be performed

    :param arr:
    :return arr:

    doc-тесты
    >>> bubble_sort([3,2,1])
    [1, 2, 3]
    """
    # внешний цикл количество проходов (длина массива - 1)
    for i in range(len(arr)-1):
        # внутренний цикл, длина массива-i-1 проходов
        for j in range(len(arr)-i-1):
            # Меняем элементы местами
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def quick_sort(arr: list):
    """
    Quicksort is an efficient sorting algorithm that relies on dividing a list into two sub-lists and selecting a pivot value.

    :param arr:
    :return arr:
    """
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


class ExternalResourceGetter:
    """
    The class accepts a link as a source, requests an html page, and returns an html page generator object
    """
    def __init__(self, url: str):
        """
        Give https-link to initialize instance

        :param url:
        """
        self.url = url
        self.data = None

    def run(self):
        self.data = self.get_data()
        result = self.parse_data()
        return result

    def get_data(self):
        response = requests.get(self.url)
        return response.text

    def parse_data(self):
        for line in self.data:
            yield line

