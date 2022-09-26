#!/usr/bin/python3

"""
A script that lists all states from the database hbtn_0e_0_usa.
- Establish a connection to mysql server and select database
- Query the database
- List results
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    sql = "SELECT * FROM states ORDER BY states.id ASC;"

    cursor.execute(sql)

    result = cursor.fetchall()

    for item in result:
        print(item)
