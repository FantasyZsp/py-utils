from canalsync.util.MyDBUtils import DBPool


def count_all_table(user: str, pw: str, ip: str, port: int, db: str):
    dbinfo = DBPool.build(user, pw, ip, port, db)
    results = dbinfo.count_all_tables()
    try:
        for res in results:
            print(res, end=' ')
    except Exception as e:
        print("error: ", e)


count_all_table('root', '123456', 'localhost', 3306, 'dbgirl')
