#!/usr/bin/env python3

import shelve

with shelve.open('people-shelve') as db:
    for key, value in db.items():
        print(key, '=>\n ', value)
