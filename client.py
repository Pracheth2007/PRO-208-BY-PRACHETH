#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import width


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
musicarea= None
labelchat = None
music_upload = None


def openChatWindow():

   
    print("\n\t\t\t\tIP MESSENGER")

    window=Tk()

    window.title('Music Window')
    window.geometry("500x350")

    global name
    global listbox
    global musicarea
    global labelchat
    global music_upload
    global filePathLabel

    namelabel = Label(window, text= "Select Song", font = ("Calibri",10))
    namelabel.place(x=10, y=8)

    name = Entry(window,width =30,font = ("Calibri",10))
    name.place(x=120,y=8)
    name.focus()

    connectserver = Button(window,text="Connect to Music Server",bd=1, font = ("Calibri",10))
    connectserver.place(x=350,y=6)

    separator = ttk.Separator(window, orient='horizontal')
    separator.place(x=0, y=35, relwidth=1, height=0.1)

    labelusers = Label(window, text= "Music Download", font = ("Calibri",10))
    labelusers.place(x=10, y=50)

    listbox = Listbox(window,height = 5,width = 67,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=70)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    connectButton=Button(window,text="Play",bd=1, font = ("Calibri",10))
    connectButton.place(x=282,y=160)

    disconnectButton=Button(window,text="Stop",bd=1, font = ("Calibri",10))
    disconnectButton.place(x=350,y=160)

    refresh=Button(window,text="Download",bd=1, font = ("Calibri",10))
    refresh.place(x=435,y=160)

    labelchat=Label(window,text="Music Uploads",font=("Calibri",10))
    labelchat.place(x=10,y=180)

    musicarea=Text(window,width=67,height=6, font=("Calibri",10))
    musicarea.place(x=10,y=200)

    scrollbar2 = Scrollbar(musicarea)
    scrollbar2.place(relheight=1,relx=1)
    scrollbar2.config(command=musicarea.yview)

    attach= Button(window, text="Attach",bd=1,font=("Calibri",10))
    attach.place(x=1,y=305)

    music_upload= Entry(window,width=43,font=("Calibri",10))
    music_upload.pack()
    music_upload.place(x=98,y=306)

    send= Button(window,text="Upload",bd=1,font=("Calibri",10))
    send.place(x=450,y=305)

    filePathLabel= Label(window,text="",fg="blue",font=("Calibri",10))
    filePathLabel.place(x=10,y=330)
  
    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    openChatWindow()

setup()
