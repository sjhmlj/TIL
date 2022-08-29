class MyClass :

    variable = '클래스변수'

    def __init__(self) :
        self.variable = '인스턴스 변수'

    def instance_method(self) :
        return self, self.instance_variable

    @classmethod 
    def class_method(cls) :
        return cls, cls.variable
    
    @staticmethod
    def static_method() :
        return 'it is static'

p = MyClass
print(p.class_method())