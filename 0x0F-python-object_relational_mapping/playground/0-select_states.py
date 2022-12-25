#!/usr/bin/env python3
''' lists all states from the database hbtn_0e_0_usa.
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

    try:
        # Execute queries
        cur.execute("SELECT * FROM states ORDER BY states.id")

        rs = cur.fetchall()

        for row in rs:
            print(row)
    except Exception as e:
        raise e
    finally:
        cur.close()
        conn.close()
