import requests


def print_5day_weather():
    print('==='+weather['result']['future'][0]['date']+'天气')
    print('城市:'+weather['result']['city'])
    print('天气:'+weather['result']['future'][0]['weather'])
    print('温度:'+weather['result']['future'][0]['temperature'])
    print('==='+weather['result']['future'][1]['date']+'天气')
    print('城市:'+weather['result']['city'])
    print('天气:'+weather['result']['future'][1]['weather'])
    print('温度:'+weather['result']['future'][1]['temperature'])
    print('==='+weather['result']['future'][2]['date']+'天气')
    print('城市:'+weather['result']['city'])
    print('天气:'+weather['result']['future'][2]['weather'])
    print('温度:'+weather['result']['future'][2]['temperature'])
    print('==='+weather['result']['future'][3]['date']+'天气')
    print('城市:'+weather['result']['city'])
    print('天气:'+weather['result']['future'][3]['weather'])
    print('温度:'+weather['result']['future'][3]['temperature'])
    print('==='+weather['result']['future'][4]['date']+'天气')
    print('城市:'+weather['result']['city'])
    print('天气:'+weather['result']['future'][4]['weather'])
    print('温度:'+weather['result']['future'][4]['temperature'])
def print_today_weather():
    print('===今日天气')
    print('城市:'+weather['result']['city'])
    print('天气:'+weather['result']['realtime']['info']+','+weather['result']['realtime']['direct'])
    print('温度:'+weather['result']['realtime']['temperature'])
    print('湿度:'+weather['result']['realtime']['humidity'])
    print('AQI:'+weather['result']['realtime']['aqi'])
def get_weather_response():
    global city,weather,Response_results
    city = input('您想查询天气的城市是:')
    url = 'http://apis.juhe.cn/simpleWeather/query?city='+city+'&key=fe83c9d941eafbbdfc16f0245e061774'#访问网址 
    response = requests.get(url)#响应结果
    weather = response.json()#json解析
    print(weather)
    if weather['reason'] == '查询成功!':
        Response_results = True
        print('输入的城市是正确的，解析中')
        print_today_weather()
        print_5day_weather()
    else:
        Response_results = False
        print('输入的城市是错误的')
        print('=== 可能是以下原因：')
        print('1.您输入的内容拼写错误，请重新输入后在查询')
        print('2.您输入的内容不是中国的城市名,因为访问的是http://apis.juhe.cn')
        print('2.您输入的内容不是城市名，有可能是省名')
get_weather_response()