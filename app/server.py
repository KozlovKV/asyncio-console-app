"""
Серверная часть приложения.
Получает от пользователя очищенные данные и производит манипуляции с хранящимися на сервере данными.
"""
import json
import os.path


class Server:
    """
    `DATA_URL` - строка относительного адреса файла словаря относительно файла запуска программы (`run.py`).
    """
    DATA_URL = './data.json'

    def __init__(self) -> None:
        self.check_json()

    def check_json(self) -> None:
        """
        Проверяет, есть ли уже файл словаря по адресу `Server.DATA_URL`.
        Если файла нет, создаёт его.
        """
        if not os.path.exists(self.DATA_URL):
            with open(self.DATA_URL, 'x') as file:
                file.write('{}')

    @property
    def data(self) -> dict:
        """
        Метод-свойство для получения всех данных из словаря.
        :return: Словарь из файла по адресу `Server.DATA_URL`.
        """
        with open(self.DATA_URL, 'r') as file:
            data = json.load(file)
            return data

    def get(self, key: str) -> [list, int]:
        """
        Получение данных по ключу

        :param key: Ключ, по которому получаются данные из словаря.
        Если `key = '*'`, возвращает все имеющиеся на сервере данные.
        Если ключа в словаре нет, возвращает -1.
        :type key: `str`
        :return: -1 либо список из словарей с ключами и всеми данными, соответствующими этим ключам.
        """
        data = self.data
        if key == '*':
            return list(data.items())
        elif data.get(key, 'error') == 'error':
            return -1
        else:
            return [[key, data[key]], ]

    def put(self, key: str, data: float, time: int) -> None:
        """
        Добавляет в словарь новую запись.

        :param key: Ключ, по которому добавляется новая запись.
        :type key: `str`

        :param data: Записываемое значение.
        :type data: `float`

        :param time: Время записи (вводится произвольно).
        :type data: `int`
        """
        new_data = self.data
        value_list = new_data.get(key, [])
        value_list += [[data, time], ]
        new_data[key] = value_list
        with open(self.DATA_URL, 'w') as file:
            json.dump(new_data, file)
