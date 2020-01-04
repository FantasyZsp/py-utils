from canalsync.util.MyDBUtils import DBPool

dbinfo = DBPool.build('root', '123456', 'localhost', 3306, 'dbgirl')
results = dbinfo.count_table_rows('girl')
results2 = dbinfo.list_all_col()
print(results2)
try:
    for res in results2:
        print(res)
except Exception as e:
    print("error: ", e)

print("=====end=====")
