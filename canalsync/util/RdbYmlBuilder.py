#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 列出所有表参考了下面的文档 https://blog.csdn.net/qq_33811662/article/details/80855430
import os
import copy
import yaml

from canalsync.util.MyDBUtils import DBPool


def represent_none(self, _):
    return self.represent_scalar('tag:yaml.org,2002:null', '')


yaml.add_representer(type(None), represent_none)


# 根据表名构建yml文件内容
# template_content深度拷贝
def build_content_case_map_all(template_content, table_name, primary_key_name):
    tmp_template_content = copy.deepcopy(template_content)
    dbMapping = tmp_template_content.get('dbMapping')
    dbMapping.update({'table': table_name})
    dbMapping.update({'targetTable': table_name})
    targetPk = dbMapping.get('targetPk')
    targetPk.clear()
    targetPk[primary_key_name] = primary_key_name
    # template_content.__setitem__('dbMapping', dbMapping)
    return tmp_template_content


# 列名 TODO 主键
def build_content_case_columns(template_content, table_name, column_names):
    dbMapping: dict = template_content.get('dbMapping')
    if dbMapping.get('mapAll', False):
        dbMapping.pop('mapAll')
    # del dbMapping['mapAll']
    dbMapping.update({'table': table_name})
    dbMapping.update({'targetTable': table_name})
    dbMapping.__setitem__('targetColumns', dict.fromkeys(column_names, None))
    return template_content


# 构建yml文件名
def build_path(dir_path, table_name):
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
def fetch_template_content(filePath: str):
    with open(filePath, 'r', encoding='UTF-8') as f:
        content = yaml.safe_load(f)
    print('template_content: ', end='')
    print(content)
    return content


def batch_generate_yml_file_test():
    prefix = 'D:/temp/pyyml_test/'
    username = "canal"  # 用户名
    password = "canal"  # 连接密码
    ip = "192.168.2.116"  # 连接地址
    port = 13306  # 连接端口
    database = "avengers_test"  # 数据库名
    databaseInfo = DBPool.build(username, password, ip, port, database)
    tables = databaseInfo.list_table()
    template_content = fetch_template_content('./template_yml/template_content_test.yml')

    for table_name in tables:
        column_names = databaseInfo.list_col(table_name)
        # file_content = build_content_case_columns(template_content, table_name, column_names)
        primary_key_name = databaseInfo.get_primary_key_name(table_name, database)
        file_content = build_content_case_map_all(template_content, table_name, primary_key_name)  # mapAll模式
        file_path = build_path(prefix + 'mapAll', 'test_' + table_name)
        generate_yml_file(file_path, file_content)


def batch_generate_yml_file_beta():
    prefix = 'D:/temp/pyyml_beta/'
    username = "canal"  # 用户名
    password = "canal"  # 连接密码
    ip = "192.168.2.116"  # 连接地址
    port = 13306  # 连接端口
    database = "avengers"  # 数据库名
    databaseInfo = DBPool.build(username, password, ip, port, database)
    tables = databaseInfo.list_table()
    template_content = fetch_template_content('./template_yml/template_content_beta.yml')

    for table_name in tables:
        # column_names = databaseInfo.list_col(table_name)
        # file_content = build_content_case_columns(template_content, table_name, column_names)
        primary_key_name = databaseInfo.get_primary_key_name(table_name, database)
        file_content = build_content_case_map_all(template_content, table_name, primary_key_name)  # mapAll模式
        file_path = build_path(prefix + 'mapAll', table_name)
        generate_yml_file(file_path, file_content)
