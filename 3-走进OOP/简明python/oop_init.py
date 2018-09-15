class Person():
    def __init__(self, aa):
        self.aa = aa

    def say_hi(self):
        print('Hello, my name is', self.aa)


p = Person('JZY')
p.say_hi()
