# batch_generate_yml_file()
#
from mysql.DBUtils import DbInfo
from mysql.EtlUtils import batch_etl

databaseInfo = DbInfo.build_dbinfo()
# 获取表名
tables = databaseInfo.list_table(databaseInfo)
# 同步
batch_etl(tables)
