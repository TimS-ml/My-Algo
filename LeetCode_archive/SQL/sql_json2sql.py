import json


def get_mysql_sql_from_leetcodejson(json_str):
    jo = json.loads(json_str)
    res = []
    for db_name in jo['headers'].keys():
        col_list = jo['headers'][db_name]
        sql = 'insert into %s (%s) values' % (db_name, ', '.join(col_list))
        # print(sql)
        values = []
        for x in jo['rows'][db_name]:
            tos = ['NULL' if y is None else '\'%s\'' % (y) for y in x]
            values.append('(%s)' % (', '.join(tos)))
        sql += ', '.join(values) + ';'
        res.append(sql)
    return res


json_str = input('input lc json:')
# json_str = '{"headers":{"student":["name","continent"]},"rows":{"student":[["Jane","America"],["Pascal","Europe"],["Xi","Asia"],["Jack","America"]]}}'

print('\n')
for sql in get_mysql_sql_from_leetcodejson(json_str):
    print(sql)
