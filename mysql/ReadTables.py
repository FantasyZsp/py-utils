#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 列出所有表参考了下面的文档 https://blog.csdn.net/qq_33811662/article/details/80855430
import pymysql
import yaml
import os


class DbInfo:
    def __init__(self, ip, username, password, database):
        self.ip = ip
        self.username = username
        self.password = password
        self.database = database


# 根据表名构建yml文件内容
def build_yml_file_content_case_map_all(template_content, table_name):
    dbMapping = template_content.get('dbMapping')
    dbMapping.update({'table': table_name})
    dbMapping.update({'targetTable': table_name})
    # template_content.__setitem__('dbMapping', dbMapping)
    return template_content


# 列名
def build_yml_file_content_case_map_columns(template_content, table_name, column_names):
    dbMapping: dict = template_content.get('dbMapping')
    if dbMapping.get('mapAll', False):
        dbMapping.pop('mapAll')
    # del dbMapping['mapAll']
    dbMapping.update({'table': table_name})
    dbMapping.update({'targetTable': table_name})
    dbMapping.__setitem__('targetColumns', dict.fromkeys(column_names, None))
    return template_content


# 构建yml文件名
def build_yml_file_path(dir_path, table_name):
    if not dir_path[-1].__eq__('/'):
        dir_path = dir_path + '/'

    if not os.path.exists(dir_path):  # 如果路径不存在
        os.makedirs(dir_path)
    return dir_path + table_name + '.yml'


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


def list_col(db_info: DbInfo, table_name):
    db = pymysql.connect(db_info.ip, db_info.username, db_info.password, db_info.database, charset="utf8")
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


def represent_none(self, _):
    return self.represent_scalar('tag:yaml.org,2002:null', '')


yaml.add_representer(type(None), represent_none)

prefix = 'D:/temp/pyyml/'
username = "root"  # 用户名
password = "123456"  # 连接密码
ip = "localhost"  # 连接地址
database = "avengers_zz"  # 数据库名
databaseInfo = DbInfo(ip, username, password, database)

tables = list_table(ip, username, password, database)  # 获取所有表，返回的是一个可迭代对象
template_content = fetch_template_content()

# for table_name in tables:
#     file_content = build_yml_file_content_case_map_all(template_content, table_name)
#     file_path = build_yml_file_path(prefix, table_name)
#     generate_yml_file(file_path, file_content)

for table_name in tables:
    column_names = list_col(databaseInfo, table_name)
    file_content = build_yml_file_content_case_map_columns(template_content, table_name, column_names)
    file_path = build_yml_file_path(prefix + 'colunms', table_name)
    generate_yml_file(file_path, file_content)
