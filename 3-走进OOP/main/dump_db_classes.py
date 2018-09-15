import shelve

db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n ', db[key].name, db[key].pay)

bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())

# 输出:
# bob =>
#   Bob Smith 30000
# sue =>
#   Sue Jones 40000
# tom =>
#   Tom Doe 50000
# Smith
# Doe
