import pymysql

config = {
    "user": "root",
    "password": "1",
    "host": "192.168.72.131",
    "database": "mysql"
}

cxn = pymysql.connect(**config)
cur = cxn.cursor(pymysql.cursors.DictCursor)
cur.execute("select * from user")
print(cur.fetchone())

