class Queue:

    def __init__(self):
        self.q = []
        self.dq = []

    def enQ(self, value):
        self.q.append(value)
        print(*self.q,sep=', ')

    def deQ(self):
        if len(self.q) == 0:
            print('Empty')
        else:
            print(f'{self.q[0]} <- ',end='')
            self.dq.append(self.q[0])
            self.q.pop(0)
            if len(self.q) == 0:
                print('Empty')
            else: print(*self.q,sep=', ')

    def end(self):
        if len(self.dq) == 0:
            print('Empty',end='')
        else:
            print(*self.dq, sep=', ',end='')
        print(' : ',end='')
        if len(self.q) == 0:
            print('Empty')
        else:
            print(*self.q, sep=', ',end='')


ip = [e for e in input("Enter Input : ").split(',')]

q = Queue()

for i in ip:
    if i == 'D':
        q.deQ()
    else:
        command, value = i.split(' ')
        q.enQ(value)

q.end()
