import pickle


# 不推荐这种方法，如果加载大数据，会很慢
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()

db['sue']['pay'] *= 1.1
db['tom']['name'] = 'Tom tom'

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
