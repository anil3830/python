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
root.mainloop()'''
#ex Lable,entry, button
from tkinter import *
hi=Tk()
hi.title('welcome')
hi.geometry('200x200')
l1=Label(hi,text='enter name',font='times 10',fg='blue',bg='green')
l1.grid(row=0,column=0)
e1=Entry(hi,font='times 11',fg='black',bg='white')
e1.grid(row=0,column=1)
b1=Button(hi,text='click',command='welcome')
b1.grid(row=0,column=2)
hi.mainloop()