class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.job = job
        self.pay = pay


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'Software')
    sue = Person('Sue Jones', 45, 40000, 'Hardware')
    print(bob.job, sue.pay)

    print(bob.name.split()[-1])
    sue.pay *= 1.1
    print(sue.pay)
