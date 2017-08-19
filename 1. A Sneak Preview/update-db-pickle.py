#!/usr/bin/env python3

import pickle

with open('people-pickle', 'rb') as db_file:
    db = pickle.load(db_file)

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

with open('people-pickle', 'wb') as db_file:
    pickle.dump(db, db_file)
