# batch_generate_yml_file()
#
from canalsync.util.MyDBUtils import DBPool
from canalsync.util.RdbYmlBuilder import batch_generate_yml_file_beta

username = "canal"  # 用户名
password = "canal"  # 连接密码
ip = "192.168.2.116"  # 连接地址
port = 13306  # 连接端口
database = "avengers"  # 数据库名

databaseInfo = DBPool.build(username, password, ip, port, database)
# 获取表名
tables = databaseInfo.list_table()

# 获取表的主键属性名
for table_name in tables:
    column = databaseInfo.get_primary_key_name(table_name, database)
    print(column)
