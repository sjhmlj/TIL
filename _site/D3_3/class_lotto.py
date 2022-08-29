import random

class lotto :
    

    def haveD(self, n) :
        number = range(1, 46)
        for i in range(n) :
            self.result = random.sample(number, 6)
            return sorted(self.result)

    def checkD(self, D_number) :
        if D_number in self.result :
            return '당첨'
        else : 
            return  '꽝', self.result
            
d1 = lotto()
d1.haveD(3)
print(d1.checkD([1, 2, 3, 4, 5, 6]))