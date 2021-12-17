"""
Клиентская часть приложения.
Отвечает за приём данных от пользователя, проверку их корректности, отправку на сервер и вывод результата
"""
from app.server import Server


class Client:
    """
    `COMMANDS` - словарь ключевых слов, каждому из которых соответствует лямбда-функция,
    запускающая необходимый метод для обработки данной команды
    """
    COMMANDS = {
        'get': lambda self, args: self.get(*args[1:]),
        'put': lambda self, args: self.put(*args[1:]),
        'error': lambda self, args: self.error(),
    }

    def __init__(self, server: Server) -> None:
        self.server = server

    def loop(self) -> None:
        """
        Основная "петля" приложения.

        Принимает команды от пользователя, делит их по пробелам и ищет команду в словаре `COMMANDS`.
        В случае пустого ввода, неверного количества аргументов или
         некорректной команды вызывает метод `Client.error()`
        """
        while True:
            args = input().strip().split()
            try:
                command = self.COMMANDS.get(args[0], self.COMMANDS['error'])
                command(self, args)
            except TypeError:
                self.error()
            except IndexError:
                self.error()

    def get(self, key: str) -> None:
        """
        Метод вывода полученных от сервера данных.

        Преобразует полученные данные из списка пар [ключ, все_записи]
        в простой список с тройками [ключ, значение, время].
        :param key: Ключ, по которому получаются данные с севера.
        Если `key = '*'`, выводит все имеющиеся на сервере данные.
        Если ключа в словаре нет, вызывается метод `Client.error()`.
        :type key: `str`
        """
        data = self.server.get(key)
        if data == -1:
            self.error()
            return
        result = []
        for note in data:
            key = note[0]
            values = note[1]
            for value in values:
                result.append(f'{key} {value[0]} {value[1]}')
        print('\n'.join(result))

    def put(self, key: str, data: str, time: str) -> None:
        """
        Метод записи данных на сервер.

        :param key: Ключ, по которому добавляется новая запись.
        :type key: `str`

        :param data: Записываемое значение.
        :type data: `str`, после преобразования должно быть `float`,
        если преобразование невозможно, вызывается метод `Client.error()`

        :param time: Время записи (вводится произвольно).
        :type data: `str`, после преобразования должно быть `int`,
        если преобразование невозможно, вызывается метод `Client.error()`
        """
        try:
            data = float(data)
            time = int(time)
        except ValueError:
            self.error()
            return
        self.server.put(key, data, time)
        print('ok')

    @staticmethod
    def error():
        """
        Статический метод вывода сообщения об ошибке
        """
        print('\nerror\nerror command\n')
