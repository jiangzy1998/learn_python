import shelve
from person import Person

fieldnames = ('name', 'age', 'job', 'pay')
db = shelve.open('class-shelve')
while True:
    key = input('\nKey? => ')
    if not key:
        break
    if key in db:
        record = db[key]        # 更新存在的记录
    else:                       # 或者创建/保存新的记录
        record = Person(name='?', age='?')
    for field in fieldnames:
        currval = getattr(record, field)                          
        newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
        if newtext:
            # eval 用来转换输入，用引号括起的字符串输入
            setattr(record, field, eval(newtext))  # eval: 引号字符串
    db[key] = record
db.close()
