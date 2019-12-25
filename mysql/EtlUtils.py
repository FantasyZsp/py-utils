import requests


def batch_etl(adapter_type: str, key: str, tablePrefix: str, tableNames: list):
    print('etl starting...')

    for table in tableNames:
        url = 'http://127.0.0.1:8081/etl' + adapter_type + key + tablePrefix + table + '.yml'
        payload = "params=2019-10-21%2000%3A00%3A00"
        print('etl ' + table + ' starting...', end=' url==> ')
        print(url)
        response = requests.request("POST", url, data=payload)
        print(response.text)


def batch_default(tableNames: list):
    adapter_type = '/rdb'
    key = '/avengers_canal/'
    tablePrefix = ''
    batch_etl(adapter_type, key, tablePrefix, tableNames)


def batch_test(tableNames: list):
    adapter_type = '/rdb'
    key = '/avengers_test_canal/'
    tablePrefix = 'test_'
    batch_etl(adapter_type, key, tablePrefix, tableNames)
