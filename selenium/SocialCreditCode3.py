import time

from selenium import webdriver

# common define
wd = webdriver.Chrome(r'./driver/chromedriver.exe')
socialCreditCodeItemXpath = '/html/body/div[2]/div/div/div[5]/div[1]/div/div[3]/div[1]/div[2]/div[2]/table[2]/tbody/tr[3]/td[2]'
companyItemFullXpath = '/html/body/div[2]/div/div[1]/div[4]/div[2]/div[1]/div/div[3]/div[1]/a'
emXpath = '/html/body/div[2]/div/div[1]/div[4]/div[2]/div[1]/div/div[3]/div[1]/a/em'

# 进入搜索页面
wd.get("https://www.tianyancha.com/search")
# 保存搜索页面的句柄
firstSearchWindow = wd.current_window_handle
searchBoxId = 'header-company-search'

# business define
isDebug = False
companyNameList = ['河南省私塾世纪教育咨询有限责任公司', '郑州中小企业担保有限公司']

for companyName in companyNameList:
    # 进行搜索
    wd.switch_to.window(firstSearchWindow)
    searchBox = wd.find_element_by_id(searchBoxId)
    searchBox.clear()
    searchBox.send_keys(companyName + '\n')
    time.sleep(1)
    companyItem = wd.find_element_by_xpath(companyItemFullXpath)
    if isDebug:
        print('连接信息: ' + companyItem.get_property('href'))
    searchNameResult = companyItem.find_element_by_xpath(emXpath).text
    if isDebug:
        print('公司名字: ' + searchNameResult)

    if searchNameResult == companyName:
        if isDebug:
            print("search success, forward details page")
        companyItem.click()
        time.sleep(1)
        # 切换到新窗口
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
            if companyName in wd.title and wd.current_url.__contains__('company'):
                break
        if isDebug:
            print(wd.title + ': ' + wd.current_url)
        socialCreditCodeItem = wd.find_element_by_xpath(socialCreditCodeItemXpath)
        socialCreditCode = socialCreditCodeItem.text
        print(companyName + ' 社会信用码: ', socialCreditCode)
        wd.close()
    else:
        print("search failed")
wd.quit()
print('test')
