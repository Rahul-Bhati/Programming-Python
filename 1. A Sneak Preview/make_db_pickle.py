#!/usr/bin/env python3

from initdata import db
import pickle

with open('people-pickle', 'wb') as db_file:
    pickle.dump(db, db_file)
