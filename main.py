import os
import numpy
import time
import random
from PIL import Image
import matplotlib.pyplot as plt 
import gc
def deal_with(myself,another):
    # 勾股定理计算需要跳跃的位移
    x1,y1 = myself
    x2,y2 = another
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    print("[INFO]需要跳跃的距离为:%d" %(distance))
    
    number = random.randint(600,700)
    print('[INFO]随机数字为:%d' %(number))
    
    
    os.system("adb shell input swipe %d %d %d %d %d" %(number,number+1,number,number+1,int(distance*1.8)))
    # 跳一跳需要distance*2.1   搭桥需要大约*1.8
    number = None
    distance = None
    x1 = None
    y1 = None
    x2 = None
    y2 = None
    gc.collect()
    # adb点击屏幕跳跃distance
    # 按压时间和跳跃距离的时间还需要计算
    # 另外点击屏幕需要随机取坐标

    #time.sleep(random.uniform(1.2,1.5))
    time.sleep(1.2)

        # 延时：因为跳跃需要时间
        #跳一跳延时：0.7,0.9
        #搭桥延时 0.9-1
        # 搭桥比跳一跳延时要长一些
    Get_Img()

def Get_Img():
    #adb截图返回图片
    os.system("adb shell screencap -p /sdcard/screencap.png")
    os.system("adb pull /sdcard/screencap.png")
    data = numpy.array(Image.open('screencap.png'))
    plt.imshow(data)
    plt.show()
    
def click(event,list1=[]):
    # 鼠标单击事件
    list1.append((event.xdata,event.ydata)) # 获取横纵坐标并加入到list1中
    if len(list1) == 2:
            print(list1)
            deal_with(list1.pop(),list1.pop())


# 主函数开头
fig = plt.figure('Snow')
fig.canvas.mpl_connect('button_press_event', click) # 挂载鼠标单击事件
# 开始执行
Get_Img()


