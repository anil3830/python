# to create window
'''from tkinter import *
window=Tk()
window.mainloop()
# to create window and title
from tkinter import *
window=Tk()
window.title('gui')
window.geometry('400x400')
window.mainloop()
#tkinter widgets are 16 typess
#  Lable this is used to display the message in window
from tkinter import *
try:
   window=Tk()
   window.title('practice')
   window.geometry('300x400')
   l1=Label(window,text='welcome',font='times 10',fg='green')
   l1.grid(row=0,column=0)
   #window.pack()
   window.mainloop()
except Exception as error:
    print('error is',error)
# entry it is used to enter the input data in window
from tkinter import *
root=Tk()
root.title('window')
root.geometry('200x300')
e1=Entry(root,font='times 15',fg='black',bg='green')
e1.grid(row=2,column=3)
root.mainloop()
#
#button this is used to press a button to perform some action
from tkinter import *
root=Tk()
root.title('file, edit')
root.geometry('200x200')
b1=Button(root,text='click',command='welcome')
#b1.grid(row=0,column=5)
b1.pack()
root.mainloop()
#ex Lable,entry, button
from tkinter import *
hi=Tk()
hi.title('welcome')
hi.geometry('400x200')
l1=Label(hi,text='enter name',font='times 10',fg='blue',bg='green')
l1.grid(row=0,column=0)
e1=Entry(hi,font='times 11')
e1.grid(row=0,column=1)
b1=Button(hi,text='click',command='display')
b1.grid(row=0,column=2)
hi.mainloop()
#adding two numbers
#
def add():
    x=int(e1.get())
    y=int(e2.get())
    z=x+y
    s.set(z)
from tkinter import *
root=Tk()
s=StringVar()
root.title('addtion')
root.geometry('400x300')
l1=Label(root,text='first number:',font='times 10')
l1.grid(row=0,column=0)
l2=Label(root,text='second number:',font='times 10')
l2.grid(row=1,column=0)
e1=Entry(root,font='times 13')
e1.grid(row=0,column=1)
e2=Entry(root,font='times 13')
e2.grid(row=1,column=1)
l3=Label(root,text='Result:',font='times 10')
l3.grid(row=2,column=0)
l4=Label(root,textvariable=s,font='times 10')
l4.grid(row=2,column=1)
b1=Button(root,text='add',font='times 12',command=add)
b1.grid(row=4,column=1)
root.mainloop()
#
#check button
#it is usefull to display number of options to user
from tkinter import *
root=Tk()
var1=IntVar()
var2=IntVar()
root.title('example')
root.geometry('400x200')
r1=Checkbutton(root,text='yes',font='times 10',variable=var1)
r1.grid(row=0,column=0)
r2=Checkbutton(root,text='no',font='times 10',variable=var2)
r2.grid(row=1,column=0)
root.mainloop()
#
#radiobutton
# it is use  to offer melti choice options to the user ,it offers seversl options but user select only one
from tkinter import *
root=Tk()
var1=IntVar()
var2=IntVar()
root.title('example')
root.geometry('400x200')
r1=Radiobutton(root,text='ece',font='times 10',variable=var1)
r1.grid(row=0,column=0)
r2=Radiobutton(root,text='cse',font='times 10',variable=var2)
r2.grid(row=1,column=0)
root.mainloop()
#
#scale
#it is used to provide a graphical slider thatr allows any value that scale
from tkinter import *
root=Tk()
root.title('hello')
root.geometry('400x300')
s=Scale(root,from_=1,to=10)
s.pack()
s1=Scale(root,from_=1,to=10,orient=HORIZONTAL)
s1.pack()
root.mainloop()
##
#list box
# it offers alist to the user from which he can accept any number of options
from  tkinter import *
root=Tk()
root.title('2313')
root.geometry('300x300')
l=Listbox(root)
l.insert(1,'python')
l.insert(2,'java')
l.insert(3,'django')
l.pack()
root.mainloop()
#
#scrollbar
# it is vartical,horixontal scroll bars it refers to slide controller which will be used to impllliment list widgets
from tkinter import *
try:
   root=Tk()
   root.geometry('300x300')
   Scrollbar=Scrollbar(root)
   Scrollbar.pack(side='right', fill='y')
   l1=Listbox(root,yscrollcommand='scrollbar.set()')
   #for line in range(100):
   l1.insert(END, str())
   l1.pack(side=LEFT,fill=BOTH)
   Scrollbar.config(command=l1.yview)
   root.mainloop()
except Exception as error:
    print('error is',error)'''
#
#menu
# it is used to create all kinds of menues used by the applications
#message
# it is use full to disply multi line text,it is non editable it is same as label it is mainly used in headings purpose
from  tkinter import *
window=Tk()
window.geometry('300x400')
s='kosmik tech hyd'
m=Message(window,text=s,font='times 12',bg='yellow',fg='green')
m.pack()
window.mainloop()
#text
# it is used to display multi line text ,it is editable
from tkinter import *
root=Tk()
t=Text(root,height=3,width=4)
t.pack()
t.insert(END,'python is heigh level language')
root.mainloop()
