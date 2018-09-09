# # 1.使用List
# bob = ['Bob Smith', 42, 30000, 'software']
# sue = ['SUe Jones', 45, 40000, 'hardware']
# print(bob[0], bob[2])       # 获取姓名 薪水
# print(bob[0].split()[-1])   # Bob姓什么? -1是指 从右边数第一个
# sue[2] *= 1.25              # 给sue加薪25%
# print(sue)


# # 2.数据库类表
# bob = ['Bob Smith', 42, 30000, 'software']
# sue = ['SUe Jones', 45, 40000, 'hardware']
# people = [bob, sue]
# for person in people:
#     print(person)
#     print(person[0].split()[-1])
#     person[2] *= 1.20
#     print(person[2])
# print(people[1][0])

# pays1 = [person[2] for person in people]  # 收集薪酬信息
# print(pays1)

# pays2 = map(lambda x: x[2], people)
# print(list(pays2))

# pays3 = sum(person[2] for person in people)  # 生成器表达式， sum为内建函数
# print(pays3)

# people.append(['Tom', 50, 0, None])
# print(len(people))
# print(people[-1][0])


# # 3.Field标签
# NAME, AGE, PAY = range(3)
# bob = ['Bob Smith', 42, 10000]
# print(bob[NAME])
# print(PAY, bob[PAY])


# bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
# sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
# people = [bob, sue]
# for person in people:
#     for (name, value) in person:
#         if name == 'name':
#             print(value)


# def field(record, label):
#     for (fname, fvalue) in record:
#         if fname == label:
#             return fvalue


# print(field(bob, 'name'))
# print(field(sue, 'pay'))
# for rec in people:
#     print('age', field(rec, 'age'))  # 打印出所有年龄


# # 4.使用字典
# bob = {'name': 'Bob Smith', 'age': 42, 'pay': 10000}
# sue = {'name': 'Sue Jones', 'age': 45, 'pay': 20000}
# print(bob['name'])
# print(bob['name'].split()[-1])
# sue['pay'] *= 1.00
# print(sue['pay'])

# # 其他建立字典的方法
# # 使用关键词关键词参数和类型构造函数
# bob = dict(name='Bob Smith', age=42, pay=10000)  # 所有的键都是字符串
# sue = dict(name='Sue Jones', age=45, pay=20000)
# print(bob)
# print(sue)


# # 一次一个字段地填写字典
# sue = {}
# sue['name'] = 'Sue Jones'
# sue['age'] = 45
# sue['pay'] = 20000
# sue['job'] = 'hardware'
# print(sue)  # 字典的键都是伪随机排列的


# # 用zip函数将名/值列表连在一起
# names = ['name', 'age', 'pay', 'job']
# values = ['Sue Jones', 45, 20000, 'hardware']
# sue = dict(list(zip(names, values)))
# print('zip', sue)

# # 通过一个键序列和所有键的可选初始值来创建字典(便于初始化空字典)
# fields = ('name', 'age', 'pay', 'job')
# record = dict.fromkeys(fields, '?')
# print(record)

# bob = dict(name='Bob Smith', age=42, pay=10000)
# sue = dict(name='Sue Jones', age=45, pay=20000)
# people = [bob, sue]
# for person in people:
#     print(person['name'], person['pay'], sep=',')
# for person in people:
#     if person['name'] == 'Sue Jones':
#         print(person['pay'])

# names = [person['name'] for person in people]
# print(names)

# print(list(map((lambda x: x['name']), people)))

# print(sum(person['pay'] for person in people))

# # 使用类似SQL查询
# print([rec['name'] for rec in people if rec['age'] > 42])

# print([(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people])

# G = (rec['name'] for rec in people if rec['age'] > 42)
# print(next(G))

# G = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
# print(G.__next__())


# # 5.嵌套结构
# bob2 = {'name': {'first': 'Bob', 'last': 'Smith'},
#         'age': 42,
#         'job': ['software', 'writing'],
#         'pay': (40000, 50000)}
# print(bob2['name'])
# print(bob2['name']['first'])
# print(bob2['pay'][1])
# for job in bob2['job']:
#     print(job)
# print(bob2['job'][-1])
# bob2['job'].append('janitor')
# print(bob2['job'])


# 6.字典的字典
bob = dict(name='Bob Smith', age=42, pay=30000, job='software')
sue = dict(name='Sue Smith', age=45, pay=40000, job='hardware')
db = {}
db['bob'] = bob
db['sue'] = sue
print(db)

print(db['bob']['name'])
db['sue']['pay'] = 50000
print(db['sue']['pay'])
import pprint           # pprint模块可以使输出更易于理解
pprint.pprint(db)

for key in db:
    print(key, '=>', db[key]['name'])

# 使用迭代字典的值集合来直接访问记录
for record in db.values():
    print(record['pay'])
x = [db[key]['name'] for key in db]
print(x)
x = [key['name'] for key in db.values()]
print(x)

# 继续添加数据
db['tom'] = dict(name='Tom', age=50, job=None, pay=0)
print(list(db.keys()))
x = [rec['name'] for rec in db.values() if rec['age'] >= 45]
print(x)
