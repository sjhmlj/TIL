## getattr() 과 같이 만들기


from re import L


class person :
    
    def __init__(self, name) :
        self.name1 = name
    
    def greeting(self) :
        print(f'안녕하세요 {self.name1} 입니다.')
        
    
        
        
        
iu = person('아이유')

# iu.name = '아이유유
print(type(getattr(iu, 'name1')))
# print(iu.name1)
# print(dir(iu))    
    
def mygetattr(a, b) :
    
    for i in dir(a) :
        if b == i :
            return str(a) + '.' + b
        
print(mygetattr(iu, 'name1'))
    
print(str(iu))