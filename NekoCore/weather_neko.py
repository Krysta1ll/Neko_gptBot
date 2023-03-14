import requests


# 修改前请务必查看和风天气api文档


def getweather(city, num):
    # 处理天气数据
    # 这里是apikey，重要
    we_key = "4b2e29110cd94ccb8cf172175aac140e"
    city_name = city
    city_url = "https://geoapi.qweather.com/v2/city/lookup?"
    we_url = "https://devapi.qweather.com/v7/weather/3d"

    # 获取地址码
    city_param = {"location": city_name, "key": we_key}
    city_res = requests.get(url=city_url, params=city_param)
    if city_res.json()['code'] == '200':
        print("地址请求成功,获取到地址码")
        city_code = city_res.json()['location'][0]['id']
    else:
        print("city get error")

    we_location = city_code
    we_param = {"location": we_location, "key": we_key}
    # 请求获取天气
    we_res = requests.get(url=we_url, params=we_param)
    if we_res.json()['code'] != '200':
        print("获取天气失败")

    # 处理天气数据
    date = we_res.json()['daily'][0]['fxDate']
    date2 = we_res.json()['daily'][2]['fxDate']

    tempMax_d1 = we_res.json()['daily'][0]['tempMax']
    tempMin_d1 = we_res.json()['daily'][0]['tempMin']
    tempMax_d2 = we_res.json()['daily'][1]['tempMax']
    tempMin_d2 = we_res.json()['daily'][1]['tempMin']

    moonPhase_d1 = we_res.json()['daily'][0]['moonPhase']

    textDay_d1 = we_res.json()['daily'][0]['textDay']
    textnight_d1 = we_res.json()['daily'][0]['textNight']
    textDay_d2 = we_res.json()['daily'][1]['textDay']
    textnight_d2 = we_res.json()['daily'][1]['textNight']

    sunrise_d1 = we_res.json()['daily'][0]['sunrise']
    sunset_d1 = we_res.json()['daily'][0]['sunset']

    # 0为明天，1为后天，2为大后天，3为月相，4为日出
    if num == 0:
        ans0 = "喵喵～！今天" + city + "的天气是这样子的喵！今天最高温是【" + tempMax_d1 + "°C】最低温是【" + tempMin_d1 + "°C】。去问了猫猫之神，他说今天白天会是" + textDay_d1 + ",晚上会是" + textnight_d1 + "喵！今天也要加油喵。。。【" + date + "】"
        print(ans0)
        return ans0
    elif num == 3:
        ans3 = "喵喵～！今天晚上将会是" + moonPhase_d1 + "喔！一起去赏月吧喵"
        print(ans3)
        return ans3
    elif num == 4:
        ans4 = "喵喵～！哇哇你想和猫猫一起看日出日落喵哇！好耶！看日出的话就要" + sunrise_d1 + "起床，看日落的话就要在" + sunset_d1 + "来找我，不许迟到喵！"
        print(ans4)
        return ans4
    elif num == 1:
        ans1 = "喵喵～！明天" + city + "的天气是这样子的喵！明天最高温是【" + tempMax_d2 + "°C】最低温是【" + tempMin_d2 + "°C】。去问了猫猫之神，他说明天白天会是" + textDay_d2 + ",晚上会是" + textnight_d2 + "喵！明天也要加油喵。。。【" + date2 + "】"
        print(ans1)
        return ans1