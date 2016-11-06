class FindPrime:
    foundPrime = 0
    primevalue = []
    #def _init_(self):
        
    
    def printPrime(self, value):
        for i in range(2,value):
            for j in range(2,i):
                if(i%j == 0):
                    self.foundPrime = self.foundPrime + 1
                    break;
            if(self.foundPrime == 0):
                self.primevalue.append(i)
            self.foundPrime = 0;
        
        for i in range(len(self.primevalue)):
            print(self.primevalue[i])