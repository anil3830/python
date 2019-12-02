m={1:'python',2:'java',3:'abc'}
for i in m:
    if 'abc'==m.get(i):
        print('true')
    else:
        print('false')
#
#symbols
#to create a in here i==rows, j= colums
for i in range(7):
    for j in range(5):
        if i==0 and j in {1,2,3}:
            print('*',end=' ')
        elif (i in(1,2,4,5,6))and (j in(0,4)):
            print('*',end=' ')
        elif i==3:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#
#creating b

for i in range(5):
    for j in range(4):
        if (i in(0,2,4))and j!=3:
            print('$',end=' ')
        elif i in (1,3)and j in (0,3):
            print("$",end=' ')
        else:
            print(' ',end=" ")
    print( )

#alphabet degins designs
# creating s
for i in range(5):
    for j in range(4):
        if i in(0,2,4):
            print('@',end=' ')
        elif i==1 and j==0:
            print('@',end=' ')
        elif i==3 and j==3:
            print('@',end=' ')
        else:
            print(' ',end=' ')
    print()

    #
    #numbwrs
x=int(input('enter how many rows u want'))
for i in range(0,x+1):
    for j in range(0,i+1):
        print(j,end='')
    print()
#
#
n=int(input('enter how many rows u want'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end='')
    print()
#
n=int(input('enter how many rowe u want'))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
#
a=int(input('enter how many rows u want'))
for i in range(a+1,0,-1):
    for j in range(i+1,0,-1):
        print(i,end='')
    print()
#string reveersing
x=input('enter a word')
x1=' '
for i in x:
    x1=i+x1
print(x1)

