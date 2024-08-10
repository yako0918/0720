import signal
from gpiozero import Button,LED

def user_release():
    print("使用者按下放開")
    led.toggle() #狀態反轉

if __name__ == '__main__': #主程式執行起點
    button = Button(pin=18) # di 名稱
    button.when_released = user_release 
    led = LED(pin=25) # do 名稱
    signal.pause()