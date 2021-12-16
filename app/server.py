import json
import os.path


class Server:
    DATA_URL = './data.json'

    def __init__(self):
        self.check_json()

    def check_json(self):
        if not os.path.exists(self.DATA_URL):
            with open(self.DATA_URL, 'x') as file:
                file.write('{}')

    @property
    def data(self):
        with open(self.DATA_URL, 'r') as file:
            data = json.load(file)
            return data

    def get(self, args):
        if args[1] == '*':
            return self.data.values()
        if self.data.get(args[1], 'error') == 'error':
            return '\nerror\nerror command\n'
        return self.data.get(args[1])

    def put(self, args):
        new_data = self.data
        value_list = new_data.get(args[1], [])
        value_list += [[args[2], args[3]], ]
        new_data[args[1]] = value_list
        with open(self.DATA_URL, 'w') as file:
            json.dump(new_data, file)
