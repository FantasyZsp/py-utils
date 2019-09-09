import yaml
import json

with open('test.yml', 'r', encoding='UTF-8') as f:
    data = yaml.safe_load(f)
print(data)
# print(json.dumps(data, ensure_ascii=False, indent=2))

paths = data.get("paths")
print('===============')
# print(paths.keys())
# print(paths.values())
'''
每个接口描述内容
httpMethod uri summary
service过程
parameters
name    located in  description required    schema 
第一种（in body）
| Name  | Located in | Description | Required | Schema                                            |
| ----- | ---------- | ----------- | -------- | ------------------------------------------------- |
| param | body       | param       | Yes      | [LoginByMobileCodeParam](#loginbymobilecodeparam) |

第二种(query)
| Name  | Located in | Description | Required | Schema |
| ----- | ---------- | ----------- | -------- | ------ |
| phone | query      | 手机号码    | Yes      | string |
| type  | query      | 类型        | Yes      | string |
| code  | query      | 验证码      | Yes      | string |
'''
for path in paths:
    # print(path)
    detailsArray = paths.get(path)
    for apiHttpMethod in detailsArray:
        print('=======fetch apis========')
        summary = detailsArray.get(apiHttpMethod).get("summary")
        if summary:
            # 构建接口开头
            print('### ' + apiHttpMethod.upper() + " " + path + " " + summary)
        else:
            raise RuntimeError('缺少接口描述')
        description = detailsArray.get(apiHttpMethod).get("description")
        if description:
            # 构建service过程
            print('> Description \n' + description)
        paramsArray = detailsArray.get(apiHttpMethod).get("parameters")
        # 构建请求参数信息
        if paramsArray:
            if len(paramsArray) > 0:
                # 构建请求参数表头
                paramsHeader = '> Parameters\n' + '| Name  | Located in | Description | Required | Schema                                        |\n' \
                                                  '| ----- | ---------- | ----------- | -------- | --------------------------------------------- |'
                print(paramsHeader)
                # 构建请求参数具体内容
                '''
                | constKey | query      | 常量类型（学历：edu,学位：degree） | Yes      | string |
                '''
                for params in paramsArray:
                    print('| ' + params.get('name'), end='')
                    inBody = params.get('in')
                    print('| ' + inBody, end='')

                    if inBody == 'query':
                        print('| ' + params.get('description'), end='')

                        print('| ', end='')
                        if params.get('required'):
                            print(params.get('required'), end='')
                        else:
                            print(False)
                        print('| ' + params.get('type') + '                                        |', end='')

                    if inBody == 'body':
                        if params.get('description'):
                            print('| ' + params.get('description'), end='')
                        print('| ', end='')
                        if params.get('required'):
                            print(params.get('required'))
                        else:
                            print('False')
                        if params.get('$ref'):
                            print('| ' + params.get('$ref') + '                                        |', end='')
    # 构建响应信息
