import pymysql
from DBUtils.PooledDB import PooledDB

# DBUtil
# 用于连接数据库，查询数据库源数据
from pymysql.connections import Connection
from pymysql.cursors import Cursor


class DBPool:

    def __init__(self, ip, port, username, password, database):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.pool = PooledDB(pymysql, 10, host=self.ip, user=self.username, passwd=self.password, db=self.database,
                             port=self.port, setsession=['SET AUTOCOMMIT = 1'])

    @staticmethod
    def build_dbinfo():
        username = "canal"  # 用户名
        password = "canal"  # 连接密码
        ip = "192.168.2.116"  # 连接地址
        port = 13306  # 连接端口
        database = "avengers"  # 数据库名
        databaseInfo = DBPool(ip, port, username, password, database)
        return databaseInfo

    @staticmethod
    def build(username, password, ip, port, database):
        databaseInfo = DBPool(ip, port, username, password, database)
        return databaseInfo

    # def connect(self):
    #     db = pymysql.connect(
    #         host=self.ip,
    #         port=self.port,
    #         user=self.username,
    #         password=self.password,
    #         database=self.database,
    #         charset="utf8")
    #     return db

    def connect(self):
        return self.pool_connect()

    def pool_connect(self):
        return self.pool.connection()

    def close(self):
        self.pool.close()

    @staticmethod
    def close_all(cur: Cursor, conn: Connection):
        cur.close()
        conn.close()

    # 列出所有的表
    def list_table(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("show tables")
        table_list = [result[0] for result in cursor.fetchall()]
        DBPool.close_all(cursor, db)
        return table_list

    def list_col(self, table_name):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("select * from %s" % table_name)
        col_name_list = [result[0] for result in cursor.description]
        cursor.close()
        connection.close()
        return col_name_list

    def list_all_col(self):
        tables = self.list_table()
        for table_name in tables:
            column_names = self.list_col(table_name)
            print(table_name, end='=======')
            print(column_names)

    def count_table_rows_fetchall(self, table_name: str):
        sql = "select count(*) as %s from %s" % (self.database + '_' + table_name, table_name)
        print(sql)
        return self.query(sql)

    def count_table_rows_description(self, table_name: str):
        connection = self.connect()
        cursor = connection.cursor()
        sql = "select count(*) as %s from %s" % (self.database + '_' + table_name, table_name)
        print(sql)
        cursor.execute(sql)
        countNum2 = cursor.description
        DBPool.close_all(cursor, connection)
        return countNum2

    # 获取别名和count结果
    def count_table_rows(self, table_name: str):
        connection = self.connect()
        cursor = connection.cursor()
        sql = "select count(*) as %s from %s" % (self.database + '_' + table_name, table_name)
        print(sql)
        cursor.execute(sql)
        description = cursor.description
        countNum = cursor.fetchall()
        DBPool.close_all(cursor, connection)
        return [description[0][0], countNum[0][0]]

    def count_all_tables(self):
        self.list_table()

    def query(self, sql: str):
        connection = self.pool_connect()
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        connection.commit()
        DBPool.close_all(cursor, connection)
        return results

    def execute(self, sql: str):
        connection = self.pool_connect()
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        connection.commit()
        DBPool.close_all(cursor, connection)
        return results

    def query_description_fetchall(self, sql: str):
        connection = self.pool_connect()
        cursor = connection.cursor()
        cursor.execute(sql)
        description = cursor.description
        results = cursor.fetchall()
        connection.commit()
        DBPool.close_all(cursor, connection)
        return description, results