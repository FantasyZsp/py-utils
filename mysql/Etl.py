import requests


def batch_etl(tableNames: list):
    print('etl starting...')

    for table in tableNames:
        url = 'http://127.0.0.1:8081/etl/rdb/mysql1/' + table + '.yml'
        payload = "params=2019-10-21%2000%3A00%3A00"
        print('etl ' + table + ' starting...',end =' url==> ')
        print(url)
        response = requests.request("POST", url, data=payload)
        print(response.text)
