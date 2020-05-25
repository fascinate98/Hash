import pickle
import os
from tkinter import *
import tkinter.messagebox
import makeHash
from tkinter import filedialog

filename = ''


def makeWindow():

    def browserButtonOnClick():
        global filename
        global firstmsg
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes=[("txt","*.*")])
        filename = filename.replace("\\","/")
        textbox.insert(0, filename)

        f = open(filename, 'r')
        firstmsg = f.read()
        f.close()

        textbox3.insert('1.0',firstmsg);

    def browserButtonOnClick1():
        global filename
        global secondmsg
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes=[("txt","*.*")])
        filename = filename.replace("\\","/")
        textbox2.insert(0, filename)

        f = open(filename, 'r')
        secondmsg = f.read()
        f.close()

        textbox4.insert('1.0', secondmsg);

    def getHashButtonOnClick():
        textbox5.insert(0, makeHash.getHash(firstmsg))
        textbox6.insert(0, makeHash.getHash(secondmsg))

    window = tkinter.Tk()

    window.title("Hash-201810841 진혜린")
    window.geometry('480x380+600+200')

    frame1 = Frame(window)
    frame1.pack(fill=X, pady=20)

    labelPath = Label(frame1, text="첫번째 텍스트", width=10)
    labelPath.pack(side=LEFT, padx=15, pady=5)

    path = ""
    textbox = Entry(frame1, width=35, textvariable=path)
    textbox.pack(side=LEFT, padx=5)

    browserbtn = Button(frame1, text="폴더 열기", width=10, command = browserButtonOnClick)
    browserbtn.pack(side=LEFT, padx=10, pady=5)



    frame2 = Frame(window)
    frame2.pack(fill=X, )

    labelPath2 = Label(frame2, text="두번째 텍스트", width=10)
    labelPath2.pack(side=LEFT, padx=15, pady=5)

    path = ""
    textbox2 = Entry(frame2, width=35, textvariable=path)
    textbox2.pack(side=LEFT, padx=5)

    browserbtn2 = Button(frame2, text="폴더 열기", width=10, command=browserButtonOnClick1)
    browserbtn2.pack(side=LEFT, padx=10, pady=5)




    frame3 = Frame(window)
    frame3.pack(fill=X, pady=10)

    textbox3 = Text(frame3, height=10, width=30)
    textbox4 = Text(frame3, height=10, width=30)
    textbox3.pack(padx = 15 , pady = 5, side=LEFT)
    textbox4.pack(padx = 5 , pady = 5, side=LEFT)



    frame4 = Frame(window)
    frame4.pack(fill=X,)

    path = ""
    textbox5 = Entry(frame4, width=30, textvariable=path)
    textbox5.pack(side=LEFT, padx=15)
    path = ""
    textbox6 = Entry(frame4, width=30, textvariable=path)
    textbox6.pack(side=LEFT, padx=5)




    frame5 = Frame(window)
    frame5.pack(fill=X, )

    browserbtn2 = Button(frame5, text="해쉬 구하기", width=25, command=getHashButtonOnClick)
    browserbtn2.pack(anchor=CENTER, padx=10, pady=30)



    window.mainloop()

makeWindow()