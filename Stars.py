'''# print BP
for i in range(6):
    for j in range(9):
        if (i in(1,3)) and (j in(1,2,6,7,8)):
            print('@',end=' ')
        elif i==2 and  j in(1,3,6,8):
            print('@',end=' ')
        elif i==4 and j in(1,3,6):
            print('@',end=' ')
        elif i==5 and j in(1,2,6):
            print('@',end=' ')
        else:
            print(' ',end=' ')
    print()

#palindrom
n=int(input('enter any number'))
t=n
b=0
while n!=0:
    a=n%10
    b=b*10+a
    n=n//10
if t==b:
    print(b,' is palindron')
else:
    print(b,'is not palindron')
# revere number
n=int(input('enter a number'))
b=0
m=n
while n!=0:
    a=n%10
    b=b*10+a
    n=n//10
print(b,'is the revers number')
#
n=int(input('enter a number'))
a=0
t=n
r=0
for i in range(1,n+1):
   if n!=0:
      a=n%10
      r=r*10+a
      n=n//10
if t==r:
    print(r,'is palindron')
   if True:
      print(r,'it is revers no of given number')
else:
    print(r,'is revers no of given number')
    print('given no is not palindrom ')

#
for i in range(5):
    for j in range(15):
        if i==0 and j in (0,1,2,4,8,10,12):
            print('@',end=' ')
        elif i==1 and j in (0,2,4,5,8,12):
            print('@',end=' ')
        elif i==2 and j in (0,1,2,4,6,8,10,12):
            print('@',end=' ')
        elif i==3 and j in (0,2,4,7,8,10,12):
            print('@',end=' ')
        elif i==4 and j in (0,2,4,8,10,12,13,14):
            print('@',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#calculator program
from tkinter import *
try:
    def bclick(numbers):
       global operator
       operator=operator + str(numbers)
       S.set(operator)
    def bclearDisplay():
       operator=""
       S.set("")
    def equall():
       global operator
       sumup=str(eval(operator))
       S.set(sumup)
       operator=""
    root=Tk()
    S=StringVar()
    root.title('calculator')
    root.geometry('300x400')
    operator=''
    t=Entry(root,font='times20',textvariable=S,bg='sky blue',bd=30,justify='right').grid(columnspan=4)

    b1=Button(root,padx=16,bd=8,fg='black',command=lambda:bclick("1"),font='times16',text='1').grid(row=1,column=0)
    b2=Button(root,padx=16,bd=8,fg='black',command=lambda:bclick("2"),font='times16',text='2').grid(row=1,column=1)
    b3=Button(root,padx=16,bd=8,fg='black',command=lambda:bclick("3"),font='times16',text='3').grid(row=1,column=2)
    addition=Button(root,padx=16,bd=8,fg='black',command=lambda:bclick("+"),font='times16',text='+').grid(row=1,column=3)
    b4=Button(root,padx=16,bd=8,fg='black',command=lambda:bclick("4"),font='times16',text='4').grid(row=2,column=0)
    b5=Button(root,padx=16,bd=8,fg='black',command=lambda:bclick("5"),font='times16',text='5').grid(row=2,column=1)
    b6=Button(root,padx=16,bd=8,fg='black',command=lambda:bclick("6"),font='times16',text='6').grid(row=2,column=2)
    multiplay=Button(root,padx=16,bd=8,fg='black',command=lambda:bclick("*"),font='times16',text='*').grid(row=2,column=3)
    b7=Button(root,padx=16,bd=8,fg='black',command=lambda:bclick("7"),font='times16',text='7').grid(row=3,column=0)
    b8=Button(root,padx=16,bd=8,fg='black',command=lambda:bclick("8"),font='times16',text='8').grid(row=3,column=1)
    b9=Button(root,padx=16,bd=8,fg='black',command=lambda:bclick("9"),font='times16',text='9').grid(row=3,column=2)
    subtraction=Button(root,padx=16,bd=8,fg='black',command=lambda:bclick("-"),font='times16',text='-').grid(row=3,column=3)
    b=Button(root,padx=16,bd=8,fg='black',command=lambda:bclick("0"),font='times16',text='0').grid(row=4,column=1)
    equall=Button(root,padx=16,bd=8,fg='black',command=equall,font='times16',text='=').grid(row=4,column=2)
    division=Button(root,padx=16,bd=8,fg='black',command=lambda:bclick("/"),font='times16',text='/').grid(row=4,column=3)
    b=Button(root,padx=16,bd=8,fg='black',command=bclearDisplay,font='times16',text='clear').grid(row=4,column=0)
except Exception as error:
    print('error is ',error)

root.mainloop()





