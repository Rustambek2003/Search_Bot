from tinydb import TinyDB
from tinydb.table import Document
db = TinyDB('db.json',indent=4)
print(db.default_table_name)

user = Document({
    'firstname':'Shaxzod',
    'job':'Developer'
    },doc_id=9)
db.insert(user)