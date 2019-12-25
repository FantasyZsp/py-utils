# batch_generate_yml_file()
#
from mysql.DBUtils import DbInfo
from mysql.EtlUtils import batch_default, batch_test
from mysql.RdbYmlBuilder import batch_generate_yml_file_test

username = "canal"  # 用户名
password = "canal"  # 连接密码
ip = "192.168.2.116"  # 连接地址
port = 13306  # 连接端口
database = "avengers_test"  # 数据库名

databaseInfo = DbInfo.build(username, password, ip, port, database)
# 获取表名
tables = databaseInfo.list_table()
# 同步
# batch_default(tables)
batch_test(tables)

# 生成yml
# batch_generate_yml_file_test()
