from person_start import Person

bob = Person('Bob Smith', 42)
sue = Person('Sue Jones', 45, 40000)

people = [bob, sue]   # 一个‘数据库’列表
for person in people:
    print(person.name, person.pay)

x = [(person.name, person.pay) for person in people]
print(x)  # [('Bob Smith', 0), ('Sue Jones', 40000)]

name = [rec.name for rec in people if rec.age > 42]    # 类似 SQL 风格的查询
print(name)  # ['Sue Jones']

age = [(rec.age ** 2 if rec.age > 42 else rec.age) for rec in people]
print(age)  # [42, 2025]
