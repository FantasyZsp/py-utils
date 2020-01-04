from canalsync.util.DBUtils import DbInfo

dbinfo = DbInfo.build('canal', 'canal', '192.168.2.116', 13306, 'avengers')
tableNames = dbinfo.list_table()
print(tableNames)
results = dbinfo.count_table_rows('call_record')
print(results)
