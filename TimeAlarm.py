from time import strftime
from tkinter import *
import time
import datetime
from pygame import mixer

root = Tk()
root.geometry("500x300")
root.title('Alarm-Clock')

def setalarm():
    alarmtime=f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if(alarmtime!=": :"):
        alarmclock(alarmtime)

def alarmclock(alarmtime):
    while True:
        time.sleep(1)
        time_now=datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now==alarmtime:
            Wakeup=Label(root, font = ('arial', 20, 'bold'), text="Wake up!Wake up!Wake up",bg="DodgerBlue2", fg="white").grid(row=6, columnspan=3)
            print("wake up!")
            mixer.init()
            mixer.music.load(r'E:\pythonprogram\loud_alarm.mp3')
            mixer.music.play()
            break
def exit_fun():
    root.destroy()
        
hrs=StringVar()
mins=StringVar()
secs=StringVar()   
greet=Label(root, font = ('arial', 20, 'bold'),text=       " Take a short nap!    ").grid(row=1, columnspan=3)
hrbtn=Entry(root, textvariable=hrs, width=5, font =('arial', 20, 'bold'))
hrbtn.grid(row=2, column=1)
minbtn=Entry(root,textvariable=mins,width=5, font = ('arial', 20, 'bold')).grid(row=2, column=2)
secbtn=Entry(root, textvariable=secs,width=5, font = ('arial', 20, 'bold')).grid(row=2, column=3)
setbtn=Button(root, text ="  set alarm"  ,command=setalarm,bg="DodgerBlue2",fg="white", font = ('arial', 20,'bold')).grid(row=4, columnspan=3)
timeleft = Label(root, font=('arial', 20, 'bold'))
timeleft.place(x=200,y=200)
exit_btn=Button(root, text="Exit",command = exit_fun,bg="Blue",fg="white",font=10)
exit_btn.place(x=200,y=250)
mainloop()
