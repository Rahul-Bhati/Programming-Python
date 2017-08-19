#!/usr/bin/env python3

from init_data import bob, sue, tom

import pickle

for (key, record) in [('bob', bob), ('sue', sue), ('tom', tom)]:
    with open(key + '.pkl', 'wb') as rec_file:
        pickle.dump(record, rec_file)
