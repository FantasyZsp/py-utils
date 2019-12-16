import csv
import os
import shutil
from threading import Thread

file_csv = csv.reader(open('D:/dev/csv/train.csv', 'r'))
sourceDir = 'D:/dev/csv/data/'
targetDir = 'D:/dev/csv/data/target/'
suffix = '.tif'
i = 0

notExistList = []
existList = []
targetList = []
# 遍历csv
for row in file_csv:

    i = i + 1
    # 忽略首行
    if i == 1:
        continue
    else:
        fileName = row[0]
        sourcePath = sourceDir + fileName + suffix
        # print(filePath)
        exists = os.path.exists(sourcePath)
        # 如果文件存在,复制到新目录
        if exists:
            existList.append(sourcePath)
            # 构建目标路径
            fileType = row[1]
            targetPath = targetDir + fileType + '/'
            targetList.append(targetPath + fileName + suffix)

            if not os.path.exists(targetPath):
                os.makedirs(targetPath)
            # print(filePath)
            # Thread(target=shutil.copy, args=[sourcePath, targetPath]).start()
            shutil.copy(sourcePath, targetPath)
        # 如果不存在
        else:
            notExistList.append(sourcePath)

print(len(existList))
print(existList)
print(notExistList)
print(targetList)
