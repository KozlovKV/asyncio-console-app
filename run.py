"""
Файл запуска приложения.
Инициализирует серверную и клиентскую часть, а затем запускает основную петлю.
"""

from app.client import Client
from app.server import Server

if __name__ == '__main__':
    server = Server()
    client = Client(server)
    client.loop()
