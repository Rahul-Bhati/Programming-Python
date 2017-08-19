#!/usr/bin/env python3

import shelve

with shelve.open('class-shelve') as db:
    for key, value in db.items():
        print(key, '=>\n ', value.name, value.pay)
