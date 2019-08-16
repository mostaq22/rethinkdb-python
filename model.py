import sys

from rethinkdb import RethinkDB
r = RethinkDB()
conn = r.connect( host="localhost", port=28015, db='rethink_python')

#create a table named authors
def migrate():
    # rdb.table_create("authors").run()
    table = r.table_create("feeds").run()
    if table:
        print("Migration Done...!!!")
def save(title=None, description=None):
    return r.table('feeds').insert({"title": title, 'description': description}).run(conn)
def get_all():
    #it's a code duplication. Some how connection is closing again and again. 
    r.connect(host="localhost", port=28015, db='rethink_python').repl()
    return r.table('feeds').changes().run()

if __name__ == "__main__":
    if sys.argv[1] == 'migrate':
        migrate()
   