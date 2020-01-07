from canalsync.util.MyDBUtils import DBPool


# 仅适用于将tinyint(n)修改为tinyint
def build_alter_sql(res: list):
    templateSql = 'ALTER TABLE {TABLE_NAME} ' \
                  'MODIFY {COLUMN_NAME} tinyint {COLUMN_DEFAULT} {NULL_OR_NOTNULL} COMMENT \' {COMMENT} \';'
    COLUMN_DEFAULT = res[5]
    isNullable = res[7]
    NULL_OR_NOTNULL = ''
    # default null
    # 不存在 default null not null ，处理成 not null
    if COLUMN_DEFAULT is None and isNullable == 'YES':
        COLUMN_DEFAULT = 'DEFAULT'
        NULL_OR_NOTNULL = 'NULL'
    elif COLUMN_DEFAULT is None and isNullable == 'NO':
        COLUMN_DEFAULT = ''
        NULL_OR_NOTNULL = 'NOT NULL'
    elif COLUMN_DEFAULT is not None and isNullable == 'NO':
        COLUMN_DEFAULT = 'DEFAULT ' + COLUMN_DEFAULT
        NULL_OR_NOTNULL = 'NOT NULL'
    elif COLUMN_DEFAULT is not None and isNullable == 'YES':
        COLUMN_DEFAULT = 'DEFAULT ' + COLUMN_DEFAULT
        NULL_OR_NOTNULL = ''
    alterSql = templateSql.format(TABLE_NAME=res[1], COLUMN_NAME=res[2], COLUMN_DEFAULT=COLUMN_DEFAULT,
                                  NULL_OR_NOTNULL=NULL_OR_NOTNULL, COMMENT=res[6])
    return alterSql


sql = 'select cc.TABLE_SCHEMA, ' \
      'cc.TABLE_NAME, ' \
      'cc.COLUMN_NAME, ' \
      'cc.COLUMN_TYPE, ' \
      'cc.DATA_TYPE, ' \
      'cc.COLUMN_DEFAULT, ' \
      'cc.COLUMN_COMMENT, ' \
      'cc.IS_NULLABLE ' \
      'from information_schema.COLUMNS as cc ' \
      'where TABLE_SCHEMA in ( \'avengers\'  ) ' \
      'and COLUMN_NAME != \'is_delete\' and COLUMN_TYPE = \'tinyint(1)\''

dbinfo = DBPool.build('canal', 'canal', '192.168.2.116', 13306, 'avengers')
results = dbinfo.query(sql)
for res in results:
    alterSql = build_alter_sql(res)
    print(alterSql)
