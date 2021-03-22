from tkinter import *
import output
from output import message

#create a window
window = Tk()
#WindowTitle
window.title("TEM")
#WindowSize
window.geometry("750x425")

def SendMessage(event):
    susers.insert(INSERT,'Hello World!\n')

#Create an UI
def LeftSideBar(width, height):
    btn1 = Button(text="Click!", cursor="hand2",height=height,width=width)
    btn1.place(x=0,y=0)
    btn2 = Button(text="Click1!",cursor="hand2",height=height,width=width)
    btn2.place(relx=0,rely=0.20)
    btn3 = Button(text="Click!", cursor="hand2",height=height,width=width)
    btn3.place(relx=0,rely=0.40)
    btn4 = Button(text="Click1!",cursor="hand2",height=height,width=width)
    btn4.place(relx=0,rely=0.60)

#Create InputOutput
def InputOutput():
    #Окно ввода
    usermsg = Text(window,width=80,height=5)
    usermsg.place(x=46,y=338)
    send = Button(text="Send",cursor="hand2",height=5,width=5,command=message.lol())
    send.place(x=700, y=338)
    send.bind("<Button-1>", SendMessage())
    #Окно вывода
    susers = Text(window,width=80,height=20,cursor="arrow",state=DISABLED)
    susers.place(x=46,y=0)



#UserInterface
LeftSideBar(5,5)
#Input&OutputMessage
InputOutput()

#End of Code
window.mainloop()



    #                                                       #
    #                                                       #
    #   Нельзя использовать. Запрещено правилами Telegram.  #
    #                       =(                              #
    #                                                       #
    #                                                       #
