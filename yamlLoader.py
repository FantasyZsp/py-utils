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

for path in paths:
    print(path)
    detailsArray = paths.get(path)
    for pathDetail in detailsArray:
        print('===============')
        summary = detailsArray.get(pathDetail).get("summary")
        if summary:
            print("summary==>" + summary)
        description = detailsArray.get(pathDetail).get("description")
        if description:
            print('description==>' + description)
        paramsArray = detailsArray.get(pathDetail).get("parameters")
        if paramsArray:
            if len(paramsArray) > 0:
                print(paramsArray)
    # print(pathDetail)
# print(paths.get("/order/type/list"))
