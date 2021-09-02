class ColorCrush2:

    def __init__(self):
        self.normalInput = []
        self.mirrorInput = []
        self.bombMirror = []
        self.bombNormalIn = []
        self.bombMirrorIn = []
        self.numOfExNormal = 0
        self.numOfExNormalSum = 0
        self.numOfExNormalAfIn = 0
        self.numOfExMirror = 0
        self.numOfFailedIn = 0
        self.numOfInterrupt = 0
        self.numOfInterruptPerR = 0
        self.bombFound = True

    def enQNormal(self,value):
        self.normalInput.append(value)

    def enQMirror(self,value):
        self.mirrorInput.append(value)

    def mirrorExplosive(self):
        self.mirrorInput.reverse()
        while self.bombFound :
            self.bombFound = False
            self.bombMirrorIn = []
            for i in range(2, len(self.mirrorInput)): # find-Bomb
                if i == 2 :
                    if self.mirrorInput[i] == self.mirrorInput[i - 1] == self.mirrorInput[i - 2]:
                        self.bombMirror.append(self.mirrorInput[i])
                        self.bombMirrorIn.append(i - 2)
                        self.bombFound = True
                elif i > 2 :
                    if self.mirrorInput[i] == self.mirrorInput[i - 1] == self.mirrorInput[i - 2] != self.mirrorInput[i - 3]:
                        self.bombMirror.append(self.mirrorInput[i])
                        self.bombMirrorIn.append(i - 2)
                        self.bombFound = True
            if self.bombFound: # Remove-Bomb
                self.bombMirrorIn.reverse()
                for i in self.bombMirrorIn:
                    self.numOfExMirror += 1
                    self.mirrorInput.pop(i)
                    self.mirrorInput.pop(i)
                    self.mirrorInput.pop(i)
        self.mirrorInput.reverse()
        self.bombFound = True

    def normalExplosive(self):
        while self.bombFound:
            self.bombFound = False
            self.bombNormalIn = []
            for i in range(2, len(self.normalInput)): # find-Normal-Bomb
                if i == 2:
                    if self.normalInput[i] == self.normalInput[i - 1] == self.normalInput[i - 2]:
                        self.numOfExNormalSum += 1
                        self.bombNormalIn.append(i - 1)
                        self.bombFound = True
                elif i > 2 :
                    if self.normalInput[i] == self.normalInput[i - 1] == self.normalInput[i - 2] != self.normalInput[i - 3]:
                        self.numOfExNormalSum += 1
                        self.bombNormalIn.append(i - 1)
                        self.bombFound = True


            if self.bombFound and len(self.bombNormalIn) > 0 and len(self.bombMirror) > 0: # Add-Interrupt
                if len(self.bombNormalIn) <= len(self.bombMirror):
                    for i in range(0,len(self.bombNormalIn)):
                        for j in range(0,len(self.bombNormalIn)):
                            self.bombNormalIn[j] += 1
                        self.normalInput.insert(self.bombNormalIn[i],self.bombMirror[i])
                        self.numOfInterrupt += 1
                        self.numOfInterruptPerR +=1
                else:
                   for i in range(0, len(self.bombMirror)):
                        for j in range(0, len(self.bombNormalIn)):
                            self.bombNormalIn[j] += 1
                        self.normalInput.insert(self.bombNormalIn[i], self.bombMirror[i])
                        self.numOfInterrupt += 1
                        self.numOfInterruptPerR += 1
                for i in range(0,self.numOfInterruptPerR):
                    self.bombMirror.pop(0)
                self.numOfInterruptPerR = 0
                    
            self.bombFound = False
            self.bombNormalIn = []
            for i in range(2, len(self.normalInput)): # find-Bomb-already-Interrupt
                if i > 2 and self.normalInput[i] == self.normalInput[i - 1] == self.normalInput[i - 2] != self.normalInput[i - 3]:
                    self.bombNormalIn.append(i - 2)
                    self.bombFound = True
                elif i == 2 and self.normalInput[i] == self.normalInput[i - 1] == self.normalInput[i - 2]:
                    self.bombNormalIn.append(i - 2)
                    self.bombFound = True
            if self.bombFound: # Remove-Bomb
                self.bombNormalIn.reverse()
                for i in self.bombNormalIn:
                    self.numOfExNormalAfIn += 1
                    self.normalInput.pop(i)
                    self.normalInput.pop(i)
                    self.normalInput.pop(i)

        self.normalInput.reverse()
        self.numOfExNormal = self.numOfExNormalSum - self.numOfInterrupt
        self.numOfFailedIn = self.numOfExNormalAfIn - self.numOfExNormal

    def showFinally(self):
        self.mirrorExplosive()
        self.normalExplosive()
        print('NORMAL :\n'+str(len(self.normalInput)))
        if len(self.normalInput) != 0:
            print(*self.normalInput,sep='')
        else:
            print("Empty")
        print(f'{self.numOfExNormal} Explosive(s) ! ! ! (NORMAL)')
        if self.numOfFailedIn != 0:
            print(f'Failed Interrupted {self.numOfFailedIn} Bomb(s)')
        print('------------MIRROR------------')
        print(': RORRIM\n'+str(len(self.mirrorInput)))
        if len(self.mirrorInput) != 0:
            print(*self.mirrorInput,sep='')
        else:
            print("ytpmE")
        print(f'(RORRIM) ! ! ! (s)evisolpxE {self.numOfExMirror}')


ipN, ipM = input("Enter Input (Normal, Mirror) : ").split(" ")

NM = ColorCrush2()

for i in ipN:
    NM.enQNormal(i)

for i in ipM:
    NM.enQMirror(i)

NM.showFinally()
