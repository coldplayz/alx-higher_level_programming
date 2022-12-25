#!/usr/bin/env python3
'''
Takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa.

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
    qry = '''SELECT cities.name
        FROM cities
            INNER JOIN states
                ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id'''

    try:
        # Execute query
        cur.execute(qry, (name,))  # SQLi-safe.

        rs = cur.fetchall()

        idx = 0
        s = ''
        for row in rs:
            if idx == 0:
                s = row[0]
            else:
                s += ', ' + row[0]
            idx += 1
        print(s)
    except Exception as e:
        raise e
    finally:
        cur.close()
        conn.close()
