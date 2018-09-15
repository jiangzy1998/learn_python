class Person:

    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return ('<%s => %s: %s, %s>' %
                (self.__class__.__name__, self.name, self.pay, self.pay))


class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith', 44)
    sue = Person('Sue Jones', 47, 40000, 'Hardward')
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(sue, sue.pay, sue.lastName())
    for obj in (bob, sue, tom):
        obj.giveRaise(.10)          # 调用该对象的giveRaise方法
        print(obj)                  # 调用通常的 __str__ 方法


# 输出:
# <Person => Sue Jones: 40000, 40000> 40000 Jones
# <Person => Bob Smith: 0.0, 0.0>
# <Person => Sue Jones: 44000.0, 44000.0>
# <Manager => Tom Doe: 60000.0, 60000.0>
