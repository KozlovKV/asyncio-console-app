class Client:
    COMMANDS = {
        'get': lambda self, args: self.get(args),
        'put': lambda self, args: self.put(args),
        'error': lambda self, args: self.error(),
    }

    def __init__(self, server):
        self.server = server

    def loop(self):
        while True:
            args = input().strip().split()
            try:
                command = self.COMMANDS.get(args[0], self.COMMANDS['error'])
                command(self, args)
            except IndexError:
                self.error()

    def get(self, args):
        if len(args) != 2:
            self.error()
            return
        data = self.server.get(args)
        result = []
        for note in data:
            for values in note[1]:
                result.append(f'{note[0]} {values[0]} {values[1]}')
        print('\n'.join(result))

    def put(self, args):
        if len(args) != 4:
            self.error()
            return
        try:
            args[2] = float(args[2])
            args[3] = int(args[3])
        except ValueError:
            self.error()
            return
        self.server.put(args)
        print('ok')

    @staticmethod
    def error():
        print('\nerror\nerror command\n')

