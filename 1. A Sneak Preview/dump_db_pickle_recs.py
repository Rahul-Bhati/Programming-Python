#!/usr/bin/env python3

import pickle, glob

for filename in glob.glob('*.pkl'):
    with open(filename, 'rb') as rec_file:
        record = pickle.load(rec_file)
        print(filename, '=>\n ', record)
