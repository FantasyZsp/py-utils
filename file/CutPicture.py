# coding: utf-8
import os.path

from PIL import Image

# 指明被遍历的文件夹
# rootdir = r'.MESSIDOR_images_all'
rootdir = r'C:/Users/zhaosp/Desktop/testRename'
'''
os.walk()可以得到一个三元tupple(parent, dirnames, filenames)。
parent：起始路径。
Dirnames：起始路径下的文件夹。
Filenames：第三个是起始路径下的文件
'''
for parent, dirnames, filenames in os.walk(rootdir):  # 遍历每一张图片
    for filename in filenames:
        # print('parent is :' + parent)
        # print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        # print('the fulll name of the file is :' + currentPath)
        img = Image.open(currentPath)
        # print(img.format, img.size, img.mode)
        # img.show()
        box1 = (399, 20, 1820, 1450)  # 设置训练集（2240*1488）左、上、右、下的像素
        # box1 = (250, 30, 1180, 960)  # 设置测试集（1440*960）左、上、右、下的像素
        image1 = img.crop(box1)  # 图像裁剪
        # image1.save(r".MESSIDOR_cut_images"+''+filename)  # 存储裁剪得到的图像
        image1.save(r"C:/Users/zhaosp/Desktop/testRename2" + '/' + filename)
