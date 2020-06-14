#-*-coding:utf-8-*-
from pyautogui import position
from PIL import Image

def main():
    img = Image.new("RGB",(1920,1080),(255,255,255))
    color = (0,0,0,0)
    try:
        while True:
            x,y = position()
            print(x,',',y)
            img.putpixel((x,y),color)
    except KeyboardInterrupt:
        img.save("a.png")

if __name__ == "__main__":
    main()