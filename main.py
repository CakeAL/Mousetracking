#-*-coding:utf-8-*-
#vision:0.1
import time

import pyautogui
from PIL import Image, ImageDraw


def main():
    sx,sy = pyautogui.size() 
    img = Image.new("RGB",(sx,sy),(255,255,255))
    draw = ImageDraw.Draw(img)
    color = (0,0,0)
    stime = time.time()
    fx,fy = pyautogui.position()
    try:
        while True:
            x,y = pyautogui.position()
            #print(x,",",y)
            draw.line((fx,fy,x,y),color,1)
            fx=x
            fy=y
    except KeyboardInterrupt:
        atime = time.time() - stime
        print("一共经过了"+str(atime)+"秒。")
        img.save("经过了"+str(atime)+"秒生成的qaq.png",)
if __name__ == "__main__":
    main()
