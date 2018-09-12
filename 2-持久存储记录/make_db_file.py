dbfilename = 'people-file'
ENDDB = 'enddb'
ENDREC = 'endrec.'
RECSEP = '=>'


def storeDbase(db, dbfilename=dbfilename):
    # 将数据库格式化保存为普通文件
    dbfile = open(dbfilename, 'w')
    for key in db:
        # print(*objects, sep=' ', end='\n', file=sys.stdout)
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()


def loadDbase(dbfilename=dbfilename):
    # 解析数据，重新构建数据库
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db


if __name__ == '__main__':
    from initdata import db
    storeDbase(db)
    # print(loadDbase())
    # loaddb = loadDbase()
    # for key in loaddb:
    #     print(key, '=>\n', loaddb[key])
    # print(loaddb['sue']['name'])
