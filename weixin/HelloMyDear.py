from weixin.utils.WeiXinUtils import *


# 5.主函数main()
def hello(wxNames, atHours, atMinutes, cityCode):
    names = wxNames
    hours = atHours
    minutes = atMinutes
    number = cityCode
    g = getYMD()
    g1 = get_iciba_everyday_chicken_soup()
    #  天气接口的网站 number为城市编号
    name = 'http://t.weather.sojson.com/api/weather/city/' + number
    #  向get_sentence 传入参数
    g2 = get_sentence(name)
    times = g2['cityInfo']
    for key, name in times.items():
        city = times['city']
        parent = times['parent']
    #  字典嵌套字典
    time1 = g2['data']
    for key, name in time1.items():
        shidu = time1['shidu']
        pm25 = time1['pm25']
        quality = time1['quality']
        ganmao = time1['ganmao']
    time1 = g2['data']
    time2 = time1.get('forecast', '不存在该键')
    time2 = time2[0]
    itchat.auto_login(hotReload=True)
    for key, name in time2.items():
        high = time2['high']
        low = time2['low']
        fx = time2['fx']
        fl = time2['fl']
        type = time2['type']
        notice = time2['type']
    #  调用微信机器人
    users = itchat.search_friends(names)  # 找到用户
    userName = users[0]['UserName']

    while True:

        t = datetime.datetime.now()
        t1 = t.strftime('%Y-%m-%d %H:%M:%S')
        hour = t.hour
        minute = t.minute
        second = t.second
        print('%d:%d:%d' % (hour, minute, second))
        if hour == hours and minute == minutes:
            itchat.send_msg("%s" % g, toUserName=userName)
            itchat.send_msg('%s' % g1, toUserName=userName)
            itchat.send_msg('所在省份：%s\n'
                            '所在城市：%s\n'
                            '今日最高温度：%s\n '
                            '今日最低温度：%s\n'
                            '风向：%s\n '
                            '风力：%s\n'
                            '湿度：%s \n'
                            'PM2.5: %s\n'
                            '空气质量：%s \n'
                            '易感指数：%s\n'
                            '天气：%s - %s ' % (parent, city, high, low, fx, fl, shidu, pm25,
                                             quality, ganmao, type, notice), toUserName=userName)
            break
        else:
            time.sleep(5)  # 延迟5秒
            continue
    itchat.run()
    time.sleep(86400)


# 5.主函数main()

if __name__ == '__main__':
    # names = input("请输入你要发送人的微信名：")
    # hours = int(input("请输入几点发送消息："))
    # minutes = int(input("请输入几分发送消息："))
    # number = input("输入所在城市的编号：")
    # hello(names, hours, minutes, number)
    names = input("请输入你要发送人的微信名：")

    hours = int(input("请输入几点发送消息："))
    minutes = int(input("请输入几分发送消息："))
    number = input("输入所在城市的编号：")

    print(names)
    print(hours)
    print(minutes)
    print(number)

    g = getYMD()
    g1 = get_iciba_everyday_chicken_soup()
    #  天气接口的网站 number为城市编号
    name = 'http://t.weather.sojson.com/api/weather/city/' + number
    #  向get_sentence 传入参数
    g2 = get_sentence(name)
    times = g2['cityInfo']
    for key, name in times.items():
        city = times['city']
        parent = times['parent']
    #  字典嵌套字典
    time1 = g2['data']
    for key, name in time1.items():
        shidu = time1['shidu']
        pm25 = time1['pm25']
        quality = time1['quality']
        ganmao = time1['ganmao']
    time1 = g2['data']
    time2 = time1.get('forecast', '不存在该键')
    time2 = time2[0]
    itchat.auto_login(hotReload=True)
    for key, name in time2.items():
        high = time2['high']
        low = time2['low']
        fx = time2['fx']
        fl = time2['fl']
        type = time2['type']
        notice = time2['type']
    #  调用微信机器人
    users = itchat.search_friends(names)  # 找到用户
    userName = users[0]['UserName']

    while True:

        t = datetime.datetime.now()
        t1 = t.strftime('%Y-%m-%d %H:%M:%S')
        hour = t.hour
        minute = t.minute
        second = t.second
        print('%d:%d:%d' % (hour, minute, second))
        if hour == hours and minute == minutes:
            itchat.send_msg("%s" % g, toUserName=userName)
            itchat.send_msg('%s' % g1, toUserName=userName)
            itchat.send_msg('所在省份：%s\n'
                            '所在城市：%s\n'
                            '今日最高温度：%s\n '
                            '今日最低温度：%s\n'
                            '风向：%s\n '
                            '风力：%s\n'
                            '湿度：%s \n'
                            'PM2.5: %s\n'
                            '空气质量：%s \n'
                            '易感指数：%s\n'
                            '天气：%s - %s ' % (parent, city, high, low, fx, fl, shidu, pm25,
                                             quality, ganmao, type, notice), toUserName=userName)
            break
        else:
            time.sleep(5)  # 延迟5秒
            continue
    itchat.run()
    time.sleep(86400)
