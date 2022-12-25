#!/usr/bin/env python3
'''
Takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.

SQLi-safe.
'''

if __name__ == '__main__':
    import MySQLdb as mdb
    import sys

    # Prepare database connection parameters
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbase = sys.argv[3]
    host = 'localhost'
    port = '3306'
    name = sys.argv[4]

    # Connect to the database
    conn = mdb.connect(host=host, user=user, passwd=passwd, db=dbase)

    # Get a cursor
    cur = conn.cursor()

    # Prepare query
    qry = '''SELECT * FROM states
        WHERE name = %s
        ORDER BY states.id'''

    try:
        # Execute query
        cur.execute(qry, (name,))  # SQLi-safe.

        rs = cur.fetchall()

        for row in rs:
            print(row)
    except Exception as e:
        raise e
    finally:
        cur.close()
        conn.close()
