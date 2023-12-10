from tkinter import *
import os

def shutdown():
    os.system("shutdown /s /t 0")

def restart():
    os.system("shutdown /r /t 0")

def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    


calltk = Tk()
calltk.title("Shutdown/Restart")
calltk.geometry("250x250")
calltk.config(bg="black")

# image path

shutdown_img = PhotoImage(file="shutdown.png")
restart_img = PhotoImage(file="restart.png")
sleep_img = PhotoImage(file="sleep.png")

# all task

shutdown_button = Button(calltk,image=shutdown_img,cursor="hand2", command=shutdown)
shutdown_button.config(bg="white")
shutdown_button.pack(pady=20)
shutdown_button.place(x=80,y=41,width=100,height=50)


restart_button = Button(calltk,image=restart_img,cursor="hand2", command=restart)
restart_button.config(bg="white")
restart_button.pack(pady=20)
restart_button.place(x=80,y=100,width=100,height=50)

sleep_button = Button(calltk,image=sleep_img, command= sleep)
sleep_button.config(bg="white")
sleep_button.pack(pady=20)
sleep_button.place(x=80,y=160,width=100,height=50)

calltk.mainloop()
