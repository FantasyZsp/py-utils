# batch_generate_yml_file()
#
from mysql.DBUtils import DbInfo
from mysql.EtlUtils import batch_default
from mysql.RdbYmlBuilder import batch_generate_yml_file_beta

username = "canal"  # 用户名
password = "canal"  # 连接密码
ip = "192.168.2.116"  # 连接地址
port = 13306  # 连接端口
database = "avengers"  # 数据库名

databaseInfo = DbInfo.build(username, password, ip, port, database)
# 获取表名
tables = databaseInfo.list_table()
# 同步
batch_default(tables)

# 生成yml
# batch_generate_yml_file_beta()
