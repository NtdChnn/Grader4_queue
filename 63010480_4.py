class LoveTest:

    def __init__(self):
        self.mQ = []
        self.yQ = []
        self.mAL = []
        self.yAL = []
        self.sAc = ['Eat','Game','Learn','Movie']
        self.sLo = ['Res.','ClassR.','SuperM.','Home']
        self.mNAc = 0
        self.mNLo = 0
        self.yNAc = 0
        self.yNLo = 0
        self.loveScore = 0
        self.STR = ''

    def enQ(self, vmQ, vyQ):
        self.mQ.append(vmQ)
        self.yQ.append(vyQ)

    def showQ(self):
        print('My   Queue = ',end='')
        print(*self.mQ,sep=', ')
        print('Your Queue = ', end='')
        print(*self.yQ, sep=', ')

    def showAcLo(self):
        for i in self.mQ:
            self.mNAc, self.mNLo = str(i).split(':')
            self.mNAc = int(self.mNAc)
            self.mNLo = int(self.mNLo)
            self.STR = self.sAc[self.mNAc] + ':' + self.sLo[self.mNLo]
            self.mAL.append(self.STR)
        print('My   Activity:Location = ',end='')
        print(*self.mAL,sep=', ')
        for i in self.yQ:
            self.yNAc, self.yNLo = str(i).split(':')
            self.yNAc = int(self.yNAc)
            self.yNLo = int(self.yNLo)
            self.STR = self.sAc[self.yNAc] + ':' + self.sLo[self.yNLo]
            self.yAL.append(self.STR)
        print('Your Activity:Location = ',end='')
        print(*self.yAL,sep=', ')

    def scoreTime(self):
        for i in range(0,len(self.mQ)):
            self.mNAc, self.mNLo = str(self.mQ[i]).split(':')
            self.yNAc, self.yNLo = str(self.yQ[i]).split(':')
            self.mNAc = int(self.mNAc)
            self.mNLo = int(self.mNLo)
            self.yNAc = int(self.yNAc)
            self.yNLo = int(self.yNLo)
            if self.mNAc == self.yNAc and self.mNLo == self.yNLo:
                self.loveScore += 4
            elif self.mNLo == self.yNLo:
                self.loveScore += 2
            elif self.mNAc == self.yNAc:
                self.loveScore += 1
            else: self.loveScore -= 5

        if self.loveScore >= 7:
            print(f'Yes! You\'re my love! : Score is {self.loveScore}.')
        elif self.loveScore > 0:
            print(f'Umm.. It\'s complicated relationship! : Score is {self.loveScore}.')
        else: print(f'No! We\'re just friends. : Score is {self.loveScore}.')


ip = [e for e in input("Enter Input : ").split(',')]

q = LoveTest()

for i in ip:
    mip, yip = i.split(' ')
    q.enQ(mip, yip)

q.showQ()
q.showAcLo()
q.scoreTime()
