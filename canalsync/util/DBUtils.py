import pymysql


# DBUtil
# 用于连接数据库，查询数据库源数据
class DbInfo:
    def __init__(self, ip, port, username, password, database):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.database = database

    @staticmethod
    def build_dbinfo():
        username = "canal"  # 用户名
        password = "canal"  # 连接密码
        ip = "192.168.2.116"  # 连接地址
        port = 13306  # 连接端口
        database = "avengers"  # 数据库名
        databaseInfo = DbInfo(ip, port, username, password, database)
        return databaseInfo

    @staticmethod
    def build(username, password, ip, port, database):
        databaseInfo = DbInfo(ip, port, username, password, database)
        return databaseInfo

    # 列出所有的表
    def list_table(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("show tables")
        table_list = [tuple[0] for tuple in cursor.fetchall()]
        db.close()
        return table_list

    def list_col(self, table_name):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("select * from %s" % table_name)
        col_name_list = [tuple[0] for tuple in cursor.description]
        db.close()
        return col_name_list

    def count_table_rows(self, table_name: str):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("select count(*) as %s from %s" % (self.database + '_' + table_name, table_name))
        countNum = cursor.fetchall()
        db.close()
        return countNum[0]

    def connect(self):
        db = pymysql.connect(
            host=self.ip,
            port=self.port,
            user=self.username,
            password=self.password,
            database=self.database,
            charset="utf8")
        return db
