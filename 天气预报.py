import requests#为调用API的库
import tkinter as tk#为显示窗口的库


#awa


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
        graphical()
        update_weather()
    else:
        Response_results = False
        print('输入的城市是错误的')
        print('=== 可能是以下原因：')
        print('1.您输入的内容拼写错误，请重新输入后在查询')
        print('2.您输入的内容不是中国的城市名,因为访问的是http://apis.juhe.cn')
        print('2.您输入的内容不是城市名，有可能是省名')
def update_weather():
    global updateweather
    url = 'http://apis.juhe.cn/simpleWeather/query?city='+city+'&key=fe83c9d941eafbbdfc16f0245e061774'#访问网址 
    response = requests.get(url)#响应结果
    updateweather = response.json()#json解析
    if  not updateweather == weather():
        weather=updateweather
        print_today_weather()
        print_5day_weather()
        graphical()
        update_weather()
    else:
        update_weather()
def graphical():
    # 显示图片
    today_weather = tk.Tk()
    today_weather.geometry("360x270")
    today_weather.title('今日天气预报')
    today_weather.iconbitmap('PY/ico.ico')
    today_weather.resizable(width=False, height=False)
    # 加载图片
    image_path = "PY/今日天气界面.png"
    image = tk.PhotoImage(file=image_path)
    label_image = tk.Label(today_weather, image=image)
    label_image.pack()
    # 添加文字
    label_weather = tk.Label(today_weather, text=weather['result']['realtime']['info'],font=("微软雅黑 Light", 10))
    label_weather.place(x=55, y=60)
    label_temp = tk.Label(today_weather, text=weather['result']['realtime']['temperature']+'度',font=("微软雅黑 Light", 10))
    label_temp.place(x=55, y=101)
    label_direct = tk.Label(today_weather, text=weather['result']['realtime']['direct'],font=("微软雅黑 Light", 10))
    label_direct.place(x=55, y=143)
    label_next_weather = tk.Label(today_weather, text=weather['result']['future'][0]['weather'],font=("微软雅黑 Light", 10))
    label_next_weather.place(x=230, y=60)
    label_next_temp = tk.Label(today_weather, text=weather['result']['future'][0]['temperature'],font=("微软雅黑 Light", 10))
    label_next_temp.place(x=230, y=101)
    label_next_direct = tk.Label(today_weather, text=weather['result']['future'][0]['direct'],font=("微软雅黑 Light", 10))
    label_next_direct.place(x=230, y=143)
    today_weather.mainloop()
get_weather_response()