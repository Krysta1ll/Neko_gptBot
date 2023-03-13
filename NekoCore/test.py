import weather_neko

str = '长沙明天天气'
str1 = str.split('明')
city = str.split('明')[0]
print(city)

weather_neko.getweather(city, 0)
