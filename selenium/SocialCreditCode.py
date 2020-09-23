import sys
import time
import openpyxl

import pandas as pd
import xlrd
from selenium import webdriver
# 读取工作簿和工作簿中的工作表
from selenium.common.exceptions import NoSuchElementException


def read_names(path, nameIndex):
    # 读取工作簿和工作簿中的工作表
    nameFile = pd.read_excel(path, header=0, skiprows=0, usecols=[nameIndex])
    myResultList = []
    for item in nameFile.values:
        myResultList.append(item[0])
    return myResultList


# data->2D list: [[companyName,code],[companyName2,code2]]
def write_to_file(dirPath, data):
    # 读取工作簿和工作簿中的工作表
    df = pd.DataFrame(data, columns=['公司名称', '社会信用代码'])
    df.to_excel(dirPath + '/' + str(round(time.time() * 1000)) + '_result' + ".xlsx", index=False)


def fetchCode(wd, myCompanyNameList):
    maxMiss = 5
    missTime = 0

    # 进入搜索页面
    wd.get("https://www.tianyancha.com/search")
    # 保存搜索页面的句柄
    firstSearchWindow = wd.current_window_handle
    myResultList = []

    first = True
    for companyName in myCompanyNameList:
        if missTime > maxMiss:
            return myResultList
        # 进行搜索
        wd.switch_to.window(firstSearchWindow)
        searchBox = wd.find_element_by_id(searchBoxId)
        searchBox.clear()
        searchBox.send_keys(companyName + '\n')
        if isDebug:
            print(wd.current_url)
        if first:
            time.sleep(1)
            first = False
        time.sleep(3)
        try:
            companyItem = wd.find_element_by_xpath(companyItemFullXpath)
        except NoSuchElementException:
            try:
                companyItem = wd.find_element_by_xpath(companyItemFullXpath2)
            except NoSuchElementException:
                try:
                    companyItem = wd.find_element_by_xpath(companyItemFullXpath3)
                except NoSuchElementException:
                    print('没找到' + companyName + ' 的信息')
                    missTime = missTime + 1
                    continue

        if isDebug:
            print('连接信息: ' + companyItem.get_property('href'))
        try:
            searchNameResult = companyItem.find_element_by_xpath(emXpath).text
        except NoSuchElementException:
            try:
                searchNameResult = companyItem.find_element_by_xpath(emXpath2).text
            except NoSuchElementException:
                try:
                    searchNameResult = companyItem.find_element_by_xpath(emXpath3).text
                except NoSuchElementException:
                    searchNameResult = 'notfound'
        if isDebug:
            print('公司名字: ' + searchNameResult)

        if searchNameResult == companyName:
            if isDebug:
                print("search success, forward details page")
            firstSearchWindow = wd.current_window_handle
            companyItem.click()
            time.sleep(5)
            # 切换到新窗口
            for handle in wd.window_handles:
                wd.switch_to.window(handle)
                if companyName in wd.title and wd.current_url.__contains__('company'):
                    break
            if isDebug:
                print(wd.title + ': ' + wd.current_url)
            try:
                socialCreditCodeItem = wd.find_element_by_xpath(socialCreditCodeItemXpath)
            except NoSuchElementException:
                socialCreditCode = '未找到'
                missTime = missTime + 1
            else:
                socialCreditCode = socialCreditCodeItem.text
            print(companyName + ' 社会信用码: ', socialCreditCode)
            myResultList.append([companyName, socialCreditCode])
            wd.close()
        else:
            missTime = missTime + 1
            print("search failed")
    wd.quit()
    return myResultList


# common define
wd = webdriver.Chrome(r'./driver/chromedriver.exe')
socialCreditCodeItemXpath = '/html/body/div[2]/div/div/div[5]/div[1]/div/div[3]/div[1]/div[2]/div[2]/table[2]/tbody/tr[3]/td[2]'
companyItemFullXpath = '/html/body/div[2]/div/div[1]/div[4]/div[2]/div[1]/div/div[3]/div[1]/a'
companyItemFullXpath2 = '/html/body/div[2]/div/div[1]/div[3]/div[2]/div/div/div[3]/div[1]/a'  # 备选，只有单条结果
companyItemFullXpath3 = '/html/body/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div[3]/div[1]/a'  # 备选，没有匹配到结果
emXpath = '/html/body/div[2]/div/div[1]/div[4]/div[2]/div[1]/div/div[3]/div[1]/a/em'
emXpath2 = '/html/body/div[2]/div/div[1]/div[3]/div[2]/div/div/div[3]/div[1]/a/em'  # 备选，只有单条结果
emXpath3 = '/html/body/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div[3]/div[1]/a/em[1]'  # 备选，没有匹配到结果
searchBoxId = 'header-company-search'

# business define
isDebug = False

companyNameList = read_names('./file/公司名字.xlsx', 1)
print(companyNameList)

# companyNameList = ['河南省私塾世纪教育咨询有限责任公司', '郑州中小企业担保有限公司']
resultList = []
try:
    resultList = fetchCode(wd=wd, myCompanyNameList=companyNameList)
except BaseException:
    print('ex occur..')
finally:
    wd.quit()
print('result:', resultList)
if resultList.__sizeof__() > 0:
    write_to_file('./file', resultList)
sys.exit()
