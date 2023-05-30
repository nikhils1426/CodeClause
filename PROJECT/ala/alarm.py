from tkinter import *
import datetime
import time
from pygame import mixer
import threading
from tkinter import messagebox

root=Tk()
root.title("Alarm Clock")
root.geometry("530x330")
root.config(bg="")

alarmtime=StringVar()
msgi=StringVar()


head=Label(root,text="Alarm Clock" ,font=("comic sans",20))
head.grid(row=0,columnspan=3,pady=10)

mixer.init()

def alaa():
    a=alarmtime.get()

    AlarmT=a
    CurrentTime=time.strftime("%H:%M")

    while AlarmT!=CurrentTime:
        CurrentTime=time.strftime("%H:%M")
           

    if AlarmT==CurrentTime:
        mixer.music.load("C:\\Users\\nikhiil\\Desktop\\pythoncode\\ala\\tone.mp3")
        mixer.music.play()
        msg=messagebox.showinfo('Info',f'{msgi.get()}')
        
        if msg=='Ok':
            mixer.music.stop() 







clock=PhotoImage(file='C:\\Users\\nikhiil\\Desktop\\pythoncode\\ala\\ala.png')


img=Label(root,image=clock)
img.grid(rowspan=4,column=0)

inputt=Label(root,text="Input time",font=('comic sans',20))
inputt.grid(row=1,column=1)

altTimee=Entry(root,textvariable=alarmtime,font=('comic sans',20),width=7)
altTimee.grid(row=1,column=2)

msg=Label(root,text="Message",font=('comics sans',20))
msg.grid(row=2,column=1,columnspan=2)

msgint=Entry(root,textvariable=msgi,font=('comic sans',20))
msgint.grid(row=3,column=1,columnspan=2)

submit=Button(root,text="SUBMIT",font=('comic sans',20),command=alaa)
submit.grid(row=4,column=1,columnspan=2)

root.mainloop()