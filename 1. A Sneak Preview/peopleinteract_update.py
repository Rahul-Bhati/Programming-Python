#!/usr/bin/env python3

# interactive updates
import shelve
from person import Person

fieldnames = ('name', 'age', 'job', 'pay')

with shelve.open('class-shelve') as db:
    while True:
        key = input('\nKey? => ')
        if not key:
            break
        if key in db:
            record = db[key]
        else:
            record = Person(name='?', age='?')

        for field in fieldnames:
            curr_val = getattr(record, field)
            new_text = input('\t[%s]=%s\n\t\tnew?=>' % (field, curr_val))

            if new_text:
                setattr(record, field, eval(new_text))

        db[key] = record