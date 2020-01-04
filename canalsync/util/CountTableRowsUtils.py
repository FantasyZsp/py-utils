from canalsync.util.DBUtils import DbInfo

dbinfo = DbInfo.build('canal', 'canal', '192.168.2.116', 13306, 'avengers')
results = dbinfo.count_table_rows('call_record')
print(results)
