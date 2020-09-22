import time

from selenium import webdriver

wd = webdriver.Chrome(r'./driver/chromedriver.exe')

wd.get("https://www.tianyancha.com/")

# 通过 full xPath
# inputElement = '/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/form/div/input'
searchBoxId = 'home-main-search'
# 通过id
companyName = '河南省私塾世纪教育咨询有限责任公司'
searchBox = wd.find_element_by_id(searchBoxId)
searchBox.send_keys(companyName + '\n')

time.sleep(2)

companyItemFullXpath = '/html/body/div[2]/div/div[1]/div[4]/div[2]/div[1]/div/div[3]/div[1]/a'
companyItem = wd.find_element_by_xpath(companyItemFullXpath)
print(companyItem.get_property('href'))
emXpath = '/html/body/div[2]/div/div[1]/div[4]/div[2]/div[1]/div/div[3]/div[1]/a/em'
print(companyItem.find_element_by_xpath(emXpath).text)

print('test')
