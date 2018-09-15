import shelve

db = shelve.open('class-shelve')
sue = db['sue']
sue.giveRaise(.25)
db['sue'] = sue  # shelve update数据，重新赋值

tom = db['tom']
tom.giveRaise(.20)
db['tom'] = tom  # shelve update数据，重新赋值
db.close()
