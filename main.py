from define import *
from tkinter import *
from tkinter import font
import os

class MAIN():
    def __init__(self, window) -> None:
        # thiet lap chieu rong, chieu dai, cach ben trai, cach ben tren
        window.geometry("{}x{}+{}+{}".format(WINDOWN_WIDTH, WINDOWN_HEIGHT, WINDOWN_POSITION_RIGHT, WINDOWN_POSITION_DOWN))
        # tieu de
        window.title('Connect PLC')
        # icon
        window.iconbitmap(os.path.join(PATH_IMAGE, 'icon.ico'))
        window.resizable(False, False)

        # -----Create label
        ip = Label(window,font=('Times New Roman',10), text="IP:").place(x=20, y=50)
        port = Label(window,font=('Times New Roman',10), text="Port:").place(x=20, y=90)
        d1 = Label(window, font=('Times New Roman',10), text="D1:").place(x=250, y=50)
        d2 = Label(window, font=('Times New Roman',10), text="D2:").place(x=250, y=90)



