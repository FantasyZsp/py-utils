import argparse
import os
import re
import shutil
from os.path import isdir

list_num = 0  # 计数器


def get_items(from_dir, dest_dir, file_suffix, level=0, sub_index=''):
    '''
    :param from_dir: 文件路径，输入要处理的文件夹
    :param dest_dir: 用于把找到的文件存起来的路径
    :param level: 递归层级
    :param sub_index: 序号
    :param file_suffix: 文件后缀
    :return: 该文件自己的编号
    '''
    global list_num
    dirs = os.listdir(from_dir)  # 获取所有的子文件夹和子文件
    subpath = [os.path.join(from_dir, dir) for dir in dirs]  # 得到所有的地址
    if level == 0 and os.path.exists(dest_dir):  # 把我们要搜索的目录中去掉用来存放目标文件的文件夹
        if subpath.__contains__(dest_dir):
            subpath.remove(os.path.abspath(dest_dir))

    for index, each_item in enumerate(subpath):
        if isdir(each_item):  # 是文件夹就继续调用原函数迭代
            get_items(each_item, dest_dir=dest_dir, file_suffix=file_suffix, level=level + 1,
                      sub_index=sub_index + str(index) + '.')

        else:
            basename = os.path.basename(each_item)  # 文件的名字
            reStr = r'^.*(\.' + file_suffix + ')$'
            if re.match(reStr, basename) is not None:
                # 匹配以 .file_suffix 结尾的所有文件
                newname = str(list_num) + '_' + basename
                # newname = basename
                # 重命名可以重写
                direct_file_name = os.path.join(dest_dir, newname)
                if not os.path.exists(direct_file_name):
                    print('正在复制%s到%s文件夹中.....' % (basename, dest_dir))
                    shutil.copyfile(each_item, direct_file_name)
                else:
                    print('%s已存在,已经跳过...' % newname)
                    pass
                list_num += 1


if __name__ == '__main__':
    '''
    获取命令行参数，必须拥有 要探测的绝对目录、需要移动的文件后缀
    '''

    parser = argparse.ArgumentParser(description='移动指定后缀的文件到特定目录')
    parser.add_argument('-f', '--from', required=True)
    parser.add_argument('-s', '--suffix', default='pdf', choices=['pdf', 'html', 'mp3'])
    parser.add_argument('-d', '--dest-dir', dest='destDir', default='current')  # 存储目录
    args = parser.parse_args()
    kvs = vars(args)
    print(kvs)
    fromDir = kvs.get('from')
    suffix: str = kvs.get('suffix')
    destDir: str = kvs.get('destDir')

    if not os.path.exists(fromDir):
        print('fromDir is not a valid path')
        exit()

    if destDir.__eq__('current'):
        currentPath = os.getcwd()
        currentDirName = os.path.basename(fromDir) + '-' + suffix.upper()
        print(currentPath)
        print(currentDirName)
        destDir = './' + currentDirName + '/'

    if not os.path.exists(destDir):
        os.makedirs(destDir)
    print('files will save to ' + destDir)
    get_items(fromDir, destDir, file_suffix=suffix)
