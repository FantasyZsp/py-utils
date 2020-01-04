import re

f = open("自动收获脚本.txt")  # 返回一个文件对象
newF = open("newScript.txt", 'w')  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法
count = 0
tempDelay = 0
newLine = ''
while line:
    newLine = line
    if line.startswith('Delay'):
        count += 1
        if count == 1:
            tempDelay = int(line.split(' ')[1].replace('-', ''))
        newLine = re.sub(r'\d+', str(tempDelay), line)
        if count % 2 == 1:
            tempDelay = tempDelay + 100
        else:
            tempDelay = tempDelay + 20
    print(newLine, end=' ')
    newF.write(newLine)
    line = f.readline()
f.close()
