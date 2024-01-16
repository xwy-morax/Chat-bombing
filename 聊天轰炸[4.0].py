import pyautogui
import time
import pyperclip
import random
#导入库
w = input("文字[1]/图片[2]请复制图片/[3]脏话/[4]诅咒/[5]空白/[6]黑:")
if w=='1':
    words = input("要说的话:")
    input("请把鼠标放在输入框，并[回车]:运行")# 设置切换窗口时准备
    次数=0
    for i in words.split("\n") * 10000000:
        print(i)
        x,y = pyautogui.position()
        pyautogui.click(x,y)
        # 提取坐标，通俗一点就是鼠标点一下这个位置,定位聊天窗口
        pyperclip.copy(i)
         # 复制到截切版上去
        pyautogui.hotkey("ctrl", "v")
        # 粘贴
        pyautogui.typewrite("\n")
        # 回车
        次数=次数+1
        time.sleep(0.3)#轰炸#0.3
        if x >= 1900:
            print('共',次数-1,'条消息')
            time.sleep(10)
            break
        # 让语速不太快
if w=='2':
    input("请把鼠标放在输入框，并[回车]:运行")
    次数=0
    while True:
        x,y = pyautogui.position()
        pyautogui.click(x,y)
        pyautogui.hotkey("ctrl", "v")
    # 粘贴
        pyautogui.hotkey("\n")
        次数=次数+1
        time.sleep(0.3)#轰炸#0.3
        if x >= 1900:
            print('共',次数-1,'条消息')
            time.sleep(10)
            break
if w=='3':
    input("请把鼠标放在输入框，并[回车]:运行")# 设置切换窗口时准备
    次数=0
    while True:
        x,y = pyautogui.position()
        pyautogui.click(x,y)
        脏话= ['***', '握草[握草神]', '*你妈', '你是*', '你有病8','深井冰','你是【niang】炮']#可更换 '' 内文字,添加: 在 ] 前加： ,'脏话' 例:.....'你有病8','脏话']
        话 = random.choice(脏话)
        pyperclip.copy(话)
        # 复制到截切版上去
        pyautogui.hotkey("ctrl", "v")
        # 粘贴
        pyautogui.typewrite("\n")
        print(话)
        # 回车
        次数=次数+1
        time.sleep(0.3)#轰炸#0.3
        if x >= 1900:
            print('共',次数-1,'条消息')
            time.sleep(10)
            break
        # 让语速不太快  
if w=='4':
    input("请把鼠标放在输入框，并[回车]:运行")# 设置切换窗口时准备
    次数=0
    while True:
        脏话= ['去48', '你幸运-999', '你头秃', '你程序bug100个', '你程序bug修不上','你单身200年']#可更换 '' 内文字,添加: 在 ] 前加： ,'脏话' 例:.....'你有病8','脏话']
        x,y = pyautogui.position()
        pyautogui.click(x,y)
        话 = random.choice(脏话)
        pyperclip.copy(话)
        # 复制到截切版上去
        pyautogui.hotkey("ctrl", "v")
        # 粘贴
        pyautogui.typewrite("\n")
        # 回车
        print(话)
        次数=次数+1
        time.sleep(0.3)#轰炸#0.3
        x,y = pyautogui.position()
        if x >= 1900:
            print('共',次数-1,'条消息')
            time.sleep(10)
            break
        # 让语速不太快  
words = ' 　　　　　　                                                                     '
if w=='5':
    input("请把鼠标放在输入框，并[回车]:运行")# 设置切换窗口时准备
    次数=0
    for i in words.split("\n") * 10000000:
        print(i)
        x,y = pyautogui.position()
        pyautogui.click(x,y)
        # 提取坐标，通俗一点就是鼠标点一下这个位置,定位聊天窗口
        pyperclip.copy(i)
         # 复制到截切版上去
        pyautogui.hotkey("ctrl", "v")
        # 粘贴
        pyautogui.typewrite("\n")
        # 回车
        次数=次数+1
        time.sleep(0.3)#轰炸#0.3
        if x >= 1900:
            print('共',次数-1,'条消息')
            time.sleep(10)
            break
        # 让语速不太快
words = '███████████████████'
if w=='6':
    input("请把鼠标放在输入框，并[回车]:运行")# 设置切换窗口时准备
    次数=0
    for i in words.split("\n") * 10000000:
        print(i)
        x,y = pyautogui.position()
        pyautogui.click(x,y)
        # 提取坐标，通俗一点就是鼠标点一下这个位置,定位聊天窗口
        pyperclip.copy(i)
         # 复制到截切版上去
        pyautogui.hotkey("ctrl", "v")
        # 粘贴
        pyautogui.typewrite("\n")
        # 回车
        次数=次数+1
        time.sleep(0.3)#轰炸#0.3
        if x >= 1900:
            print('共',次数-1,'条消息')
            time.sleep(10)
            break
        # 让语速不太快







    
