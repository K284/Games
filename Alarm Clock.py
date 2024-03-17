from tkinter import *
from datetime import datetime
import time
import  winsound 
from threading import *

root = Tk()
Label(root, text = "Alarm Clock", font = ("arial",20, "bold"), fg = "dark blue").pack(pady = 10)
Label(root, text = "Set Alarm", font = ("arial",15,"bold")).pack()

def Threading():
    t1 = Thread(target = alarm)
    t1.start()

def alarm():
    while True:
        set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
        time.sleep(1)
        current_time = datetime.now().strftime("%H:%M:%S")
        if  set_time == current_time:
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)

frame = Frame()
frame.pack()

hour = StringVar()
hrs = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"]
hr = OptionMenu(frame, hour, *hrs)
hr.pack(side = LEFT)
hour.set(hrs[0])

min = StringVar()
mns = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60"]
mn = OptionMenu(frame, min, *mns)
mn.pack(side = LEFT)
min.set(mns[0])

sec= StringVar()
scs = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60"]
sc = OptionMenu(frame, sec, *scs)
sc.pack(side = LEFT)
sec.set(scs[0])


Button(root, text = "SET", font = ("arial",20, "bold"), command = Threading()).pack(pady=20)
root.mainloop()

