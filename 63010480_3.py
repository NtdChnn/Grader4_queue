class SecretMQueue:

    def __init__(self):
        self.Sq = []
        self.Nq = []
        self.newSq = []
        self.deCode = 0
        self.enCode = 0

    def enSq(self, value):
        self.Sq.append(str(value))

    def enNq(self, value):
        self.Nq.append(int(value))

    def enC(self):
        self.newSq = self.Sq.copy()
        self.Sq = []
        for i in range(0,len(self.newSq)):
            self.enCode = ord(self.newSq[i]) + self.Nq[i%len(self.Nq)]
            if 65 <= ord(self.newSq[i]) <= 90 and self.enCode > 90:
                self.enCode -= 26
            elif 97 <= ord(self.newSq[i]) <= 122 and self.enCode > 122:
                self.enCode -= 26
            self.Sq.append(str(chr(self.enCode)))
        print(f'Encode message is :  {self.Sq}')

    def deC(self):
        self.newSq = self.Sq.copy()
        self.Sq = []
        for i in range(0,len(self.newSq)):
            self.deCode = ord(self.newSq[i]) - self.Nq[i%len(self.Nq)]
            if 65 <= ord(self.newSq[i]) <= 90 and self.deCode < 65:
                self.deCode += 26
            elif 97 <= ord(self.newSq[i]) <= 122 and self.deCode < 97 :
                self.deCode += 26
            self.Sq.append(str(chr(self.deCode)))
        print(f'Decode message is :  {self.Sq}')


ipS,ipN = input('Enter String and Code : ').split(',')

sm = SecretMQueue()

for i in ipS:
    if i != ' ':
        sm.enSq(i)

for i in ipN:
    sm.enNq(i)

sm.enC()
sm.deC()

