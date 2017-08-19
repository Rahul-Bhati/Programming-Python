#!/usr/bin/env python3
"""
Save in-memory database object to a file with custom formatting; assume 'endrec.',
'enddb.', and '=>' are not used in the data; assume db is dict of dict;
warning: eval can be dangerous - it runs strings as code; could also eval()
record dict all at once; could also dbfile.write(key + '\n') vs print(key, file=dbfile);
"""

db_file_name = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'


def store_database(db, db_file_name=db_file_name):
    """formatted dump of database to flat file"""

    with open(db_file_name, 'w') as db_file:
        for key in db:
            print(key, file=db_file)
            for (name, value) in db[key].items():
                print(name + RECSEP + repr(value), file=db_file)
            print(ENDREC, file=db_file)
        print(ENDDB, file=db_file)


def load_dbase(db_file_name=db_file_name):
    """parse data to reconstruct database"""

    with open(db_file_name) as db_file:
        import sys
        sys.stdin = db_file
        db = {}
        key = input()
        while key != ENDDB:
            rec = {}
            field = input()
            while field != ENDREC:
                name, value = field.split(RECSEP)
                rec[name] = eval(value)
                field = input()

            db[key] = rec
            key = input()
        return db




if __name__ == '__main__':
    from initdata import db
    store_database(db)
