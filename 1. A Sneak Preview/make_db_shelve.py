#!/usr/bin/env python3

from init_data import bob, sue, tom
import shelve

with shelve.open('people-shelve') as db:
    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom

