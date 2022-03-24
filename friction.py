from tkinter import *
from tkinter import ttk
import math

from PIL import ImageTk, Image

sr=1
wt=0
ang=15
pan=0
muv=0.5
sum='NAN'

class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground


def viewtablef():
    global sr
    sr=1
    ws = Tk()
    ws.title('viewtable')
    ws.geometry('600x210')
    ws['bg'] = 'white'

    # tableframe = Frame(ws)
    # tableframe.pack()

    # scrollbar
    scorll = Scrollbar(ws)
    scorll.pack(side=RIGHT, fill=X)

    scorll = Scrollbar(ws, orient='horizontal')
    scorll.pack(side=BOTTOM, fill=Y)
    global table
    table = ttk.Treeview(ws, yscrollcommand=scorll.set, xscrollcommand=scorll.set)

    scorll.config(command=table.yview)
    scorll.config(command=table.xview)

    # define our column

    table['columns'] = ('SR.NO', 'SURFACE OF SLIDER', 'WEIGHT OF PAN', 'WEIGHT OF BLOCK', 'COEFFICIENT OF FRICTION')

    # format our column
    table.column("#0", width=0, stretch=NO)
    table.column("SR.NO", anchor=CENTER, width=40)
    table.column("SURFACE OF SLIDER", anchor=CENTER, width=120)
    table.column("WEIGHT OF PAN", anchor=CENTER, width=120)
    table.column("WEIGHT OF BLOCK", anchor=CENTER, width=120)
    table.column("COEFFICIENT OF FRICTION", anchor=CENTER, width=160)

    # Create Headings
    table.heading("#0", text="", anchor=CENTER)
    table.heading("SR.NO", text="SR.NO", anchor=CENTER)
    table.heading("SURFACE OF SLIDER", text="SURFACE OF SLIDER", anchor=CENTER)
    table.heading("WEIGHT OF PAN", text="WEIGHT OF PAN", anchor=CENTER)
    table.heading("WEIGHT OF BLOCK", text="WEIGHT OF BLOCK", anchor=CENTER)
    table.heading("COEFFICIENT OF FRICTION", text="COEFFICIENT OF FRICTION", anchor=CENTER)
    # add data
    table.pack()
    ws.mainloop()



def addtotablef():
    global sr
    if (muv == 0.5):
        check = "Rubber"
    else:
        check = "Aluminium"

    table.insert('', END,
                 values=(sr, check, pan, wt, sum))
    sr+=1

def murubber():
    global muv
    muv=0.5
    angrad=ang*math.pi/180
    mattype=Label(friction,text='Rubber      ',background='white',font=('Helvatical bold',25))
    mattype.place(x=200, y=650)
    if (pan > (muv * wt * math.cos(angrad)) + (wt * math.sin(angrad))):
        if (ang == 15):
            img2 = Image.open("Friction_15deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 30):
            img2 = Image.open("Friction_30deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 45):
            img2 = Image.open("Friction_45deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_short.png")
            img.paste(img2, (0, 0))

    else:
        if (ang == 15):
            img2 = Image.open("Friction_15deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 30):
            img2 = Image.open("Friction_30deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 45):
            img2 = Image.open("Friction_45deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_long.png")
            img.paste(img2, (0, 0))

def mualu():
    global muv
    muv=1.4
    angrad=ang*math.pi/180
    mattype = Label(friction, text='Aluminium ', background='white', font=('Helvatical bold', 25))
    mattype.place(x=200, y=650)
    if (pan > (muv * wt * math.cos(angrad)) + (wt * math.sin(angrad))):
        if (ang == 15):
            img2 = Image.open("Friction_15deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 30):
            img2 = Image.open("Friction_30deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 45):
            img2 = Image.open("Friction_45deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_short.png")
            img.paste(img2, (0, 0))

    else:
        if (ang == 15):
            img2 = Image.open("Friction_15deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 30):
            img2 = Image.open("Friction_30deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 45):
            img2 = Image.open("Friction_45deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_long.png")
            img.paste(img2, (0, 0))
def resetu():
    global ang
    ang=15
    global wt
    wt=0
    global pan
    pan=0
    global muv
    muv = 0.5
    global sum
    sum = 0
    global sr
    sr=1
    img2 = Image.open("Friction_15deg_long.png")
    img.paste(img2, (0, 0))
    inanglabel = Label(friction, text=ang, font=30, bg='white')
    inwtlabel = Label(friction, text=str(wt)+"   ", font=30, bg='white')
    inpanlabel = Label(friction, text=str(pan)+"   ", font=30, bg='white')
    mattype = Label(friction, text='Rubber      ', background='white', font=('Helvatical bold', 25))
    suml = Label(friction, text="                                          ", font=30, bg='white')
    suml.place(x=110, y=460)
    mattype.place(x=200, y=650)
    inanglabel.place(x=125, y=375)
    inwtlabel.place(x=130, y=102)
    inpanlabel.place(x=160, y=245)
    for item in table.get_children():
        table.delete(item)


def weightplus():
    global wt
    wt+=100
    wtlbl = Label(friction, text=wt, font=30,bg='white')
    wtlbl.place(x=130, y=102)
    global ang
    angrad = ang * math.pi / 180
    if (pan >= (muv * wt * math.cos(angrad)) + wt * math.sin(angrad)):
        if (ang == 15):
            img2 = Image.open("Friction_15deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 30):
            img2 = Image.open("Friction_30deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 45):
            img2 = Image.open("Friction_45deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_short.png")
            img.paste(img2, (0, 0))
    else:
        if (ang == 15):
            img2 = Image.open("Friction_15deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 30):
            img2 = Image.open("Friction_30deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 45):
            img2 = Image.open("Friction_45deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_long.png")
            img.paste(img2, (0, 0))

def weightmin():
    global wt
    if(wt>0):
        wt-=100
        wtlbl = Label(friction, text=str(wt)+"   ", font=30,bg='white')
        wtlbl.place(x=130, y=102)
        global ang
        angrad = ang * math.pi / 180
        if (pan > (muv * wt * math.cos(angrad)) + (wt * math.sin(angrad))):
            if (ang == 15):
                img2 = Image.open("Friction_15deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 30):
                img2 = Image.open("Friction_30deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 45):
                img2 = Image.open("Friction_45deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 60):
                img2 = Image.open("Friction_60deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 75):
                img2 = Image.open("Friction_75deg_short.png")
                img.paste(img2, (0, 0))

        else:
            if (ang == 15):
                img2 = Image.open("Friction_15deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 30):
                img2 = Image.open("Friction_30deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 45):
                img2 = Image.open("Friction_45deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 60):
                img2 = Image.open("Friction_60deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 75):
                img2 = Image.open("Friction_75deg_long.png")
                img.paste(img2, (0, 0))

def angminus():
    global ang
    if(ang>15):
        ang-=15
        anglbl=Label(friction,text=ang,font=30,bg='white')
        anglbl.place(x=125,y=375)
        if(ang==15):
            img2 = Image.open("Friction_15deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 30):
            img2 = Image.open("Friction_30deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 45):
            img2 = Image.open("Friction_45deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_long.png")
            img.paste(img2, (0, 0))


def angplus():
    global ang
    if(ang<75):
        ang+=15
        anglbl=Label(friction,text=ang,font=30,bg='white')
        if(ang==30):
            img2=Image.open("Friction_30deg_long.png")
            img.paste(img2,(0,0))
        elif(ang==45):
            img2 = Image.open("Friction_45deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_long.png")
            img.paste(img2, (0, 0))
        anglbl.place(x=125,y=375)

def calcu():
    global ang
    global wt
    global pan
    global img
    global canva
    global sum
    angrad = ang * math.pi / 180
    if(pan==wt*math.sin(angrad)):
        suml=Label(friction,text="change any value           ",font=30,bg='white')
        suml.place(x=110, y=457)
    else:
        sum=((pan-(wt*math.sin(angrad)))/(wt*math.cos(angrad)))
        sum=abs(sum)
        if(abs((sum-muv))<muv*5/100):
            suml=Label(friction,text=str(sum)+"      ",font=30,bg='white',fg='green')
            suml.place(x=110,y=457)
        elif(abs((sum-muv))<muv/10):
            suml = Label(friction, text=str(sum)+"   ", font=30, bg='white', fg='orange')
            suml.place(x=110, y=457)
        else:
            suml = Label(friction, text=str(sum)+"    ", font=30, bg='white', fg='red')
            suml.place(x=110, y=457)


def panplus100():
    global pan
    pan+=100
    panlbl = Label(friction, text=str(pan)+"   ", font=30, bg='white')
    panlbl.place(x=160, y=245)
    global ang
    angrad = ang * math.pi / 180
    if (pan >= (muv * wt * math.cos(angrad)) + wt * math.sin(angrad)):
        if (ang == 15):
            img2 = Image.open("Friction_15deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 30):
            img2 = Image.open("Friction_30deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 45):
            img2 = Image.open("Friction_45deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_short.png")
            img.paste(img2, (0, 0))
    else:
        if (ang == 15):
            img2 = Image.open("Friction_15deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 30):
            img2 = Image.open("Friction_30deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 45):
            img2 = Image.open("Friction_45deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_long.png")
            img.paste(img2, (0, 0))

def panplus25():
    global pan
    pan+=25
    global ang
    angrad = ang * math.pi / 180
    panlbl = Label(friction, text=str(pan)+"   ", font=30, bg='white')
    panlbl.place(x=160, y=245)
    if (pan >= (muv * wt * math.cos(angrad)) + (wt * math.sin(angrad))):
        if (ang == 15):
            img2 = Image.open("Friction_15deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 30):
            img2 = Image.open("Friction_30deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 45):
            img2 = Image.open("Friction_45deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_short.png")
            img.paste(img2, (0, 0))

    else:
        if (ang == 15):
            img2 = Image.open("Friction_15deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 30):
            img2 = Image.open("Friction_30deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 45):
            img2 = Image.open("Friction_45deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_long.png")
            img.paste(img2, (0, 0))
def panplus5():
    global pan
    pan+=5
    global ang
    angrad = ang * math.pi / 180
    panlbl = Label(friction, text=str(pan)+"   ", font=30, bg='white')
    panlbl.place(x=160, y=245)
    if (pan >= (muv * wt * math.cos(angrad)) + (wt * math.sin(angrad))):
        if (ang == 15):
            img2 = Image.open("Friction_15deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 30):
            img2 = Image.open("Friction_30deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 45):
            img2 = Image.open("Friction_45deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_short.png")
            img.paste(img2, (0, 0))
    else:
        if (ang == 15):
            img2 = Image.open("Friction_15deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 30):
            img2 = Image.open("Friction_30deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 45):
            img2 = Image.open("Friction_45deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_long.png")
            img.paste(img2, (0, 0))
def panplus1():
    global pan
    pan+=1
    global ang
    angrad = ang * math.pi / 180
    panlbl = Label(friction, text=str(pan)+"   ", font=30, bg='white')
    panlbl.place(x=160, y=245)
    if (pan >= (muv * wt * math.cos(angrad)) + (wt * math.sin(angrad))):
        if (ang == 15):
            img2 = Image.open("Friction_15deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 30):
            img2 = Image.open("Friction_30deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 45):
            img2 = Image.open("Friction_45deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_short.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_short.png")
            img.paste(img2, (0, 0))
    else:
        if (ang == 15):
            img2 = Image.open("Friction_15deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 30):
            img2 = Image.open("Friction_30deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 45):
            img2 = Image.open("Friction_45deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 60):
            img2 = Image.open("Friction_60deg_long.png")
            img.paste(img2, (0, 0))
        elif (ang == 75):
            img2 = Image.open("Friction_75deg_long.png")
            img.paste(img2, (0, 0))


def panminus100():
    global pan
    global ang
    angrad = ang * math.pi / 180
    if (pan>99):
        pan-=100
        panlbl = Label(friction, text=str(pan)+"   ", font=30,bg='white')
        panlbl.place(x=160, y=245)
        if (pan <=((muv * wt * math.cos(angrad)) + (wt * math.sin(angrad)))):
            if (ang == 15):
                img2 = Image.open("Friction_15deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 30):
                img2 = Image.open("Friction_30deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 45):
                img2 = Image.open("Friction_45deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 60):
                img2 = Image.open("Friction_60deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 75):
                img2 = Image.open("Friction_75deg_long.png")
                img.paste(img2, (0, 0))
        else:
            if (ang == 15):
                img2 = Image.open("Friction_15deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 30):
                img2 = Image.open("Friction_30deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 45):
                img2 = Image.open("Friction_45deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 60):
                img2 = Image.open("Friction_60deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 75):
                img2 = Image.open("Friction_75deg_short.png")
                img.paste(img2, (0, 0))
    else:
        pan=0
        panlbl = Label(friction, text=str(pan)+"   ", font=30,bg='white')
        panlbl.place(x=160, y=245)
def panminus25():
    global pan
    global ang
    angrad = ang * math.pi / 180
    if (pan>24):
        pan-=25
        panlbl = Label(friction, text=str(pan)+"   ", font=30,bg='white')
        panlbl.place(x=160, y=245)
        if (pan <=((muv * wt * math.cos(angrad)) + (wt * math.sin(angrad)))):
            if (ang == 15):
                img2 = Image.open("Friction_15deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 30):
                img2 = Image.open("Friction_30deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 45):
                img2 = Image.open("Friction_45deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 60):
                img2 = Image.open("Friction_60deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 75):
                img2 = Image.open("Friction_75deg_long.png")
                img.paste(img2, (0, 0))
        else:
            if (ang == 15):
                img2 = Image.open("Friction_15deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 30):
                img2 = Image.open("Friction_30deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 45):
                img2 = Image.open("Friction_45deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 60):
                img2 = Image.open("Friction_60deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 75):
                img2 = Image.open("Friction_75deg_short.png")
                img.paste(img2, (0, 0))
    else:
        pan=0
        panlbl = Label(friction, text=str(pan)+"   ", font=30,bg='white')
        panlbl.place(x=160, y=245)
def panminus5():
    global pan
    global ang
    angrad = ang * math.pi / 180
    if (pan>4):
        pan-=5
        panlbl = Label(friction, text=str(pan)+"   ", font=30,bg='white')
        panlbl.place(x=160, y=245)
        if (pan <=((muv * wt * math.cos(angrad)) + (wt * math.sin(angrad)))):
            if (ang == 15):
                img2 = Image.open("Friction_15deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 30):
                img2 = Image.open("Friction_30deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 45):
                img2 = Image.open("Friction_45deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 60):
                img2 = Image.open("Friction_60deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 75):
                img2 = Image.open("Friction_75deg_long.png")
                img.paste(img2, (0, 0))
        else:
            if (ang == 15):
                img2 = Image.open("Friction_15deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 30):
                img2 = Image.open("Friction_30deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 45):
                img2 = Image.open("Friction_45deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 60):
                img2 = Image.open("Friction_60deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 75):
                img2 = Image.open("Friction_75deg_short.png")
                img.paste(img2, (0, 0))
    else:
        pan=0
        panlbl = Label(friction, text=str(pan)+"   ", font=30,bg='white')
        panlbl.place(x=160, y=245)
def panminus1():
    global pan
    global ang
    angrad = ang * math.pi / 180
    if (pan>0):
        pan-=1
        panlbl = Label(friction, text=str(pan)+"   ", font=30,bg='white')
        panlbl.place(x=160, y=245)
        if (pan <=((muv * wt * math.cos(angrad)) + (wt * math.sin(angrad)))):
            if (ang == 15):
                img2 = Image.open("Friction_15deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 30):
                img2 = Image.open("Friction_30deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 45):
                img2 = Image.open("Friction_45deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 60):
                img2 = Image.open("Friction_60deg_long.png")
                img.paste(img2, (0, 0))
            elif (ang == 75):
                img2 = Image.open("Friction_75deg_long.png")
                img.paste(img2, (0, 0))
        else:
            if (ang == 15):
                img2 = Image.open("Friction_15deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 30):
                img2 = Image.open("Friction_30deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 45):
                img2 = Image.open("Friction_45deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 60):
                img2 = Image.open("Friction_60deg_short.png")
                img.paste(img2, (0, 0))
            elif (ang == 75):
                img2 = Image.open("Friction_75deg_short.png")
                img.paste(img2, (0, 0))
    else:
        pan=0
        panlbl = Label(friction, text=str(pan)+"   ", font=30,bg='white')
        panlbl.place(x=160, y=245)


friction = Tk()
friction.geometry("1080x720")
friction.title("FRICTION")
canva = Canvas(friction, width=1080, height=720)
img = ImageTk.PhotoImage(Image.open("Friction_15deg_long.png"))
canva.create_image(10, 10, anchor=NW, image=img)
inanglabel = Label(friction,text='15 ',font=30,bg='white')
inwtlabel = Label(friction,text=str(wt)+"   ",font=30,bg='white')
inpanlabel = Label(friction,text=str(pan)+"   ",font=30,bg='white')
wtlabl = Label(friction,text='WEIGHT OF BLOCK',font=('Helvatical bold',25),foreground='blue',background='white')
panlabl = Label(friction,text='WEIGHT OF PAN',font=('Helvatical bold',25),fg='blue',bg='white')
anglabl = Label(friction,text='ANGLE OF INCLINATION',font=('Helvatical bold',25),fg='blue',bg='white')
pluspn100 = HoverButton(friction , text = '+100', command = panplus100,background='white',padx=2,pady=2, activeforeground='blue',highlightthickness=0,borderwidth=0)
minpn100 = HoverButton(friction , text = '-100',padx=2,pady=2 ,command = panminus100,background='white',activeforeground='blue',borderwidth=0)
pluspn25 = HoverButton(friction , text = '+25',padx=2,pady=2,borderwidth=0 , command = panplus25,background='white',activeforeground='blue')
minpn25 = HoverButton(friction , text = '-25',padx=2,pady=2 , borderwidth=0,command = panminus25,background='white',activeforeground='blue')
pluspn5 = HoverButton(friction , text = '+5',padx=2,pady=2,borderwidth=0 , command = panplus5,background='white',activeforeground='blue')
minpn5 = HoverButton(friction , text = '-5',padx=2,pady=2 , borderwidth=0,command = panminus5,background='white',activeforeground='blue')
pluspn1 = HoverButton(friction , text = '+1',padx=2,pady=2,borderwidth=0 , command = panplus1,background='white',activeforeground='blue')
minpn1 = HoverButton(friction , text = '-1',padx=2,pady=2 , borderwidth=0,command = panminus1,background='white',activeforeground='blue')
pluswt = HoverButton(friction , text = '+100',padx=2,pady=2 ,borderwidth=0, command = weightplus,background='white',activeforeground='blue')
minwt = HoverButton(friction,text='-100',command=weightmin,borderwidth=0,padx=2,pady=2 ,background='white',activeforeground='blue')
minang = HoverButton(friction,text='-15',command=angminus,borderwidth=0,padx=2,pady=2,background='white',activeforeground='blue')
plusang = HoverButton(friction,text='+15',command=angplus,borderwidth=0,padx=2,pady=2,background='white',activeforeground='blue')
calc = HoverButton(friction,text='CALC',command=calcu,borderwidth=0,padx=2,pady=2,background='white',activeforeground='blue')
reset = HoverButton(friction,text='RESET',command=resetu,padx=2,pady=2,borderwidth=0,bg='white',activeforeground='blue')
quiit = HoverButton(friction,text="QUIT", command =friction.destroy,padx=2,pady=2,borderwidth=0,bg='white',activeforeground='blue')
mu = Label(friction,text='μ :',font=('Helvatical bold',25),fg='blue',bg='white')
rubber = HoverButton(friction,text='RUBBER',command=murubber,padx=2,pady=2,borderwidth=0,background='white',activeforeground='blue')
aluminium = HoverButton(friction,text='ALUMINIUM',command=mualu,padx=2,pady=2,borderwidth=0,background='white',activeforeground='blue')
material = Label(friction,text='MATERIAL : ',background='white',font=('Helvatical bold',25),fg='blue',activeforeground='blue')
viewtable = HoverButton(friction,text='View Table',command=viewtablef,padx=2,pady=2,borderwidth=0,background='white',activeforeground='blue')
addtotable = HoverButton(friction,text='Add To Table',command=addtotablef,padx=2,pady=2,borderwidth=0,background='white',activeforeground='blue')
if(muv == 0.5):
    type = 'Rubber'
else:
    type = 'Aluminium'
mattype = Label(friction,text=type,background='white',font=('Helvatical bold',25))
selectmaterial = Label(friction,text="SELECT MATERIAL",font=('Helvatical bold',25),bg='white',fg='blue')

canva.place(x=0,y=0)
quiit.place(x=122,y=500)
calc.place(x=40,y=500)
minang.place(x=60,y=375)
plusang.place(x=160,y=375)
pluswt.place(x=180,y=100)
minwt.place(x=60,y=100)
inanglabel.place(x=125,y=375)
inwtlabel.place(x=130,y=102)
inpanlabel.place(x=160, y=245)
panlabl.place(x=25,y=170)
anglabl.place(x=25,y=330)
pluspn100.place(x=60,y=220)
minpn100.place(x=60,y=270)
pluspn25.place(x=125,y=220)
minpn25.place(x=125,y=270)
pluspn5.place(x=180,y=220)
minpn5.place(x=180,y=270)
pluspn1.place(x=230,y=220)
minpn1.place(x=230,y=270)
wtlabl.place(x=25,y=50)
reset.place(x=200,y=500)
mu.place(x=50,y=450)
rubber.place(x=50,y=600)
aluminium.place(x=175,y=600)
selectmaterial.place(x=30,y=550)
material.place(x=50,y=650)
mattype.place(x=200,y=650)
viewtable.place(x=500,y=650)
addtotable.place(x=700,y=650)
friction.mainloop()
