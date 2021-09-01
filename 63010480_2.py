class Queue:

    def __init__(self):
        self.q = []
        self.index = 0

    def ENq(self, value):
        self.q.append(value)

    def ESq(self, value):
        self.q.insert(self.index,value)
        self.index += 1

    def deQ(self):
        if len(self.q) == 0:
            print('Empty')
        else:
            print(int(self.q[0]))
            self.q.pop(0)
        if self.index > 0:
            self.index -= 1


ip = [e for e in input("Enter Input : ").split(',')]

q = Queue()

for i in ip:
    if i == 'D':
        q.deQ()
    else:
        command, value = i.split(' ')
        if command == 'EN':
            q.ENq(value)
        else:
            q.ESq(value)
