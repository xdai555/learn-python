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


class DBManage:
    def __init__(self, db_info, db_name) -> None:
        self.db_name = db_name
        self.info = db_info
        self.conn = None
        self.cursor = None
        self.connect()
    
    def connect(self):
        try:
            db_user = self.info['db_user']
            db_host = self.info['db_host']
            db_port = int(self.info['db_port'])
            db_name = self.db_name
            db_pwd = self.info['db_password']

            self.conn = pymysql.connect(
                host=db_host,
                user=db_user,
                passwd=db_pwd,
                database=db_name,
                port=db_port)
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        except Exception as e:
            raise e
        
    def close(self):
        self.cursor.close()
        self.conn.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    
    def exec_sql(self, sql):
        """执行 SQL，以字典的方式获取执行结果

        Args:
            sql (str): 原生 SQL 语句

        Returns:
            list: 字典组成的执行结果列表，其中字典的 Key 为数据库表头，Value 为数据。
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
