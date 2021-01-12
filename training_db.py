import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE users(
    name TEXT,
    sex INTEGER,
    old INTEGER,
    score INTEGER
    )""")
    cur.execute("SELECT * FROM users WHERE old IN (19,32) AND score <= 1000 OR sex=1")
    result = cur.fetchall()
