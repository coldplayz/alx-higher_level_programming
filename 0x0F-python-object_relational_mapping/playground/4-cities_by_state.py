#!/usr/bin/env python3
'''
Lists all cities from the database hbtn_0e_4_usa.

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

    # Connect to the database
    conn = mdb.connect(host=host, user=user, passwd=passwd, db=dbase)

    # Get a cursor
    cur = conn.cursor()

    # Prepare query
    qry = '''SELECT cities.id, cities.name, states.name
        FROM cities
            INNER JOIN states
                ON cities.state_id = states.id
        ORDER BY cities.id'''

    try:
        # Execute query
        cur.execute(qry)  # SQLi-safe.

        rs = cur.fetchall()

        for row in rs:
            print(row)
    except Exception as e:
        raise e
    finally:
        cur.close()
        conn.close()
