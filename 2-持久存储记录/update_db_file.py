from make_db_file import loadDbase, storeDbase

db = loadDbase()
db['sue']['pay'] *= 1.1
db['tom']['name'] = 'Tom tom'
storeDbase(db)
