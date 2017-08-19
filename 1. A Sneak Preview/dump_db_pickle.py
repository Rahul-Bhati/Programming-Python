#!/usr/bin/env python3

import pickle

with open('people-pickle', 'rb') as db_file:
    db = pickle.load(db_file)

    for key, value in db.items():
        print(key, '=>\n ', value)
    print(db['sue']['name'])
