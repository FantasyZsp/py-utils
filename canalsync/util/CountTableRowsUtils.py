from canalsync.util.MyDBUtils import DBPool


def count_all_table(user: str, pw: str, ip: str, port: int, db: str):
    dbinfo = DBPool.build(user, pw, ip, port, db)
    results = dbinfo.count_all_tables()
    try:
        for res in results:
            print(res)
    except Exception as e:
        print("error: ", e)


def find_error_sync():
    dbinfo = DBPool.build('canal', 'canal', '192.168.2.116', 13306, 'avengers')
    results = dbinfo.count_mater_slave_all_tables_rows(
        'avengers', 'miracle')

    a = 0
    b = 0
    a_name = ''
    b_name = ''

    for idx, res in enumerate(results, 1):
        if idx % 4 == 1:
            a_name = res
        elif idx % 4 == 2:
            b_name = res
        elif idx % 4 == 3:
            a = res
        elif idx % 4 == 0:
            b = res
            if a != b:
                print(a_name, a, b_name, b)


# count_all_table('canal', 'canal', '192.168.2.116', 13306, 'avengers')
#
# print("================================")
# count_all_table('canal', 'canal', '192.168.2.116', 13306, 'miracle')

find_error_sync()
