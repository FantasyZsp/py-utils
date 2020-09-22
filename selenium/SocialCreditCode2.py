import time

from selenium import webdriver

# common define
wd = webdriver.Chrome(r'./driver/chromedriver.exe')
socialCreditCodeItemXpath = '/html/body/div[2]/div/div/div[5]/div[1]/div/div[3]/div[1]/div[2]/div[2]/table[2]/tbody/tr[3]/td[2]'

# business define
companyName = '河南省私塾世纪教育咨询有限责任公司'

wd.get("https://www.tianyancha.com/search?key=" + companyName)

# 保存搜索页面的句柄
firstSearchWindow = wd.current_window_handle
searchBoxId = 'header-company-search'
wd.switch_to.window(firstSearchWindow)
searchBox = wd.find_element_by_id(searchBoxId)
searchBox.clear()
# 进行搜索
searchBox.send_keys(companyName + '\n')

time.sleep(2)

companyItemFullXpath = '/html/body/div[2]/div/div[1]/div[4]/div[2]/div[1]/div/div[3]/div[1]/a'
companyItem = wd.find_element_by_xpath(companyItemFullXpath)
print(companyItem.get_property('href'))
emXpath = '/html/body/div[2]/div/div[1]/div[4]/div[2]/div[1]/div/div[3]/div[1]/a/em'
searchNameResult = companyItem.find_element_by_xpath(emXpath).text
print(searchNameResult)

if searchNameResult == companyName:
    print("search success, forward details page")

    companyItem.click()
    time.sleep(1)
    # 切换到新窗口
    for handle in wd.window_handles:
        wd.switch_to.window(handle)

        if companyName in wd.title and wd.current_url.__contains__('company'):
            break

    print(wd.title + ': ' + wd.current_url)
    socialCreditCodeItem = wd.find_element_by_xpath(socialCreditCodeItemXpath)
    socialCreditCode = socialCreditCodeItem.text
    print('socialCreditCode: ', socialCreditCode)


else:
    print("search failed")

print('test')
