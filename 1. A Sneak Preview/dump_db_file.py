#!/usr/bin/env python3

from make_db_file import load_dbase

db = load_dbase()

for key in db:
    print(key, '=>\n ', db[key])
    print(db['sue']['name'])
