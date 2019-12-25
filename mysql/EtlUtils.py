import requests
from mysql.DBUtils import DbInfo


def batch_etl(tableNames: list):
    print('etl starting...')

    # type = '/rdb'
    # key = '/avengers_test_canal/'
    # tablePrefix = 'test_'

    type = '/rdb'
    key = '/avengers_canal/'
    tablePrefix = ''

    for table in tableNames:
        # url = 'http://127.0.0.1:8081/etl/rdb/mysql1/' + table + '.yml'
        url = 'http://127.0.0.1:8081/etl' + type + key + tablePrefix + table + '.yml'
        payload = "params=2019-10-21%2000%3A00%3A00"
        print('etl ' + table + ' starting...', end=' url==> ')
        print(url)
        response = requests.request("POST", url, data=payload)
        print(response.text)
