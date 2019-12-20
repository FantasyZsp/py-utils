#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 列出所有表参考了下面的文档 https://blog.csdn.net/qq_33811662/article/details/80855430
import pymysql

# 查询所有字段
import yaml


# 根据表名构建yml文件内容
def build_yml_file_content(template_content, table_name):
    dbMapping = template_content.get('dbMapping')
    dbMapping.update({'table': table_name})
    dbMapping.update({'targetTable': table_name})
    # template_content.__setitem__('dbMapping', dbMapping)
    return template_content


# 构建yml文件名
def build_yml_file_path(prefix, table_name):
    return prefix + table_name + '.yml'


# 生成yml文件
def generate_yml_file(target_file_path, yml_content):
    with open(target_file_path, 'w', encoding='UTF-8') as template_file:
        yaml.dump(yml_content, template_file, default_flow_style=False, sort_keys=False)
    # print(yml_content)


# 获取模板内容
def fetch_template_content():
    with open('template_content.yml', 'r', encoding='UTF-8') as f:
        content = yaml.safe_load(f)
    print('template_content: ', end='')
    print(content)
    return content


def list_col(ip, username, password, database, table_name):
    db = pymysql.connect(ip, username, password, database, charset="utf8")
    cursor = db.cursor()
    cursor.execute("select * from %s" % table_name)
    col_name_list = [tuple[0] for tuple in cursor.description]
    db.close()
    return col_name_list


# 列出所有的表
def list_table(ip, username, password, database):
    db = pymysql.connect(ip, username, password, database, charset="utf8")
    cursor = db.cursor()
    cursor.execute("show tables")
    table_list = [tuple[0] for tuple in cursor.fetchall()]
    db.close()
    return table_list


prefix = 'D:/temp/pyyml/'
username = "root"  # 用户名
password = "123456"  # 连接密码
localhost = "localhost"  # 连接地址
database = "avengers_zz"  # 数据库名
tables = list_table(localhost, username, password, database)  # 获取所有表，返回的是一个可迭代对象
# print(tables)

# for table in tables:
#     col_names = list_col(localhost, username, password, database, table)
#     print(col_names)  # 输出所有字段名

template_content = fetch_template_content()

i = 0
for table_name in tables:
    file_content = build_yml_file_content(template_content, table_name)
    file_path = build_yml_file_path(prefix, table_name)
    generate_yml_file(file_path, file_content)
