#!/usr/bin/env python3

import shelve
from init_data import tom

with shelve.open('people-shelve') as db:
    sue = db['sue']
    sue['pay'] *= 1.50
    db['sue'] = sue
    print(type(db['sue']['pay']))
    db['tom'] = tom
    db.clear()
    del db['tom']
