import shelve


class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.job = job
        self.pay = pay


fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)

bob = Person('Bob Smith', 22, 30000, 'Software')
sue = Person('Sue Jones', 25, 40000, 'Hardware')
tom = Person('Tom Doe', 20, 50000)
db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom


while True:
    key = input('\nKey? => ')
    if not key:
        break
    try:
        record = db[key]
    except TypeError:  # 一定要指明要捕捉的错误类型，不要使用空的except语句。
        print('No such key "%s"!' % key)
    else:
        for field in fieldnames:
            # ljust 使输出的字符串左对齐,并使用空格填充至指定长度的新字符串
            # getattr 来获取对象的属性
            print(field.ljust(maxfield), '=>', getattr(record, field))
