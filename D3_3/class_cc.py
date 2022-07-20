from re import L


class Person :
    name ='주현'

    def __init__(self, name) :
      self.name1 = name
    
    def greeting(self) :
        print(f'안녕하세요 {self.name1}입니다')
      

p1 = Person('조르바')

print(Person.name)
p1.greeting()