import socket


class RpnCalculator:

    memory = []

    def push_value(self, num):
        self.memory.insert(0, num)

    def pop_value(self):
        return self.memory.pop(0)

    def add(self):
        sum = self.memory.pop(0) + self.memory.pop(0)
        self.memory.insert(0, sum)


s = socket.socket()
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(5)

calc = RpnCalculator()

client, address = s.accept()
print('Connection from', address)

while True:

    total_cmd = client.recv(1024)

    cmd, num = total_cmd.split(' ')

    if cmd == 'pop':
        client.send(calc.pop_value())

    elif cmd == 'add':
        calc.add()
        client.send('added')

    elif cmd == 'push':
        calc.push_value(int(num))
        client.send('pushed')
    else:
        client.send('invalid cmd')

