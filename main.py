import time
import pgzrun
import pygame
import requests
#from random import randint
disp_time = ""
HEIGHT = 720
WIDTH = 1280
TITLE = "Clock"
disp_time1 = ["0","0","0"]
weather = "更新中"
ms = 0.00
update_time = time.localtime(0)
weather_status = "更新中..."
city = "Newyork"
temp2 = True

def update_weather(city=):
    global weather,update_time,weather_status
    try:
        rb = requests.get(f'http://wthrcdn.etouch.cn/weather_mini?city={city}')
        rb = rb.json()
        weather = [f"今天{rb['data']['forecast'][0]['high']}，{rb['data']['forecast'][0]['low']}，{rb['data']['forecast'][0]['fengxiang']}，{rb['data']['forecast'][0]['type']}。",
                   f"明天{rb['data']['forecast'][1]['high']}，{rb['data']['forecast'][1]['low']}，{rb['data']['forecast'][1]['fengxiang']}，{rb['data']['forecast'][1]['type']}。",
                   f"后天{rb['data']['forecast'][2]['high']}，{rb['data']['forecast'][2]['low']}，{rb['data']['forecast'][2]['fengxiang']}，{rb['data']['forecast'][2]['type']}。"]
        update_time = time.localtime(time.time())
        weather_status = "更新于{}年{}月{}日，{}时{}分{}秒。".format(update_time[0],update_time[1],update_time[2],update_time[3],update_time[4],update_time[5])
    except:
        weather_status = "更新失败..."

def update():
    global disp_time,disp_time1,temp1,date,temp2
    disp_time = time.localtime(time.time())
    if temp2:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        temp2 = False
    if len(str(disp_time[3])) == 1:
        disp_time1[0] = "0"+str(disp_time[3])
    else:
        disp_time1[0] = str(disp_time[3])
    if len(str(disp_time[4])) == 1:
        disp_time1[1] = "0"+str(disp_time[4])
    else:
        disp_time1[1] = str(disp_time[4])
    if len(str(disp_time[5])) == 1:
        disp_time1[2] = "0"+str(disp_time[5])
    else:
        disp_time1[2] = str(disp_time[5])
    temp1 = True
    get_ms()
    date1 = time.localtime(time.time())
    if date1[6] == 0:
        wday = "星期一"
    elif date1[6] == 1:
        wday = "星期二"
    elif date1[6] == 2:
        wday = "星期三"
    elif date1[6] == 3:
        wday = "星期四"
    elif date1[6] == 4:
        wday = "星期五"
    elif date1[6] == 5:
        wday = "星期六"
    elif date1[6] == 6:
        wday = "星期日"
    date = [date1[0],date1[1],date1[2],wday]

def get_ms():
    global ms
    ms1 = time.time()
    ms1 = str(int((ms1 - float(int(ms1))) * 100))
    if len(str(ms1)) == 1:
        ms = f"0{ms1}"
    else:
        ms = ms1

def draw():
    global temp1,disp_time1,weather,ms,date,update_time,weather_status,WIDTH,HEIGHT
    screen.clear()
    screen.draw.text(weather[0],(20,550),fontsize=30,fontname="mc.ttf",color="gold")
    screen.draw.text(weather[1],(20,590),fontsize=30,fontname="mc.ttf",color="blue")
    screen.draw.text(weather[2],(20,630),fontsize=30,fontname="mc.ttf",color="red")
    screen.draw.text("{}:{}:{}".format(disp_time1[0],disp_time1[1],disp_time1[2]),(180,260),fontsize=170,fontname="mc.ttf")
    #screen.draw.text("Made by Bilibili@SALTWOOD",(20,20),fontsize=20,fontname="mc.ttf",color=(randint(50,255),randint(50,255),randint(50,255)))
    screen.draw.text(ms,(1030,347),fontsize=70,fontname="mc.ttf",color="white")
    screen.draw.text("{}年{}月{}日，{}".format(date[0],date[1],date[2],date[3]),(180,210),fontsize=40,fontname="mc.ttf",color="white")
    screen.draw.text(weather_status,(20,520),fontsize=25,fontname="mc.ttf",color="green")

def on_mouse_down(pos):
    global weather
    weather = "更新中"
    update_weather()
    #print(pos)

def on_key_down(key):
    if key == keys.F:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif key == keys.W:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))

update_weather(city)
clock.schedule_interval(update_weather,1800)
pgzrun.go()
