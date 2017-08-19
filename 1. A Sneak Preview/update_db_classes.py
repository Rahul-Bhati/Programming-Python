#!/usr/bin/env python3

import shelve

with shelve.open('class-shelve') as db:
    sue = db['sue']
    sue.give_raise(.5)
    db['sue'] = sue

    tom = db['tom']
    tom.give_raise(.1)
    db['tom'] = tom

