#to create a list and perform following operation
#insertion,deletion,display,exit
l=[]
while True:
    print('1 for insertion')
    print('2 for delrtion')
    print('3 for display')
    print('4 for exit')
    s=int(input('enter which option u want'))
    if s==1:
        n=int(input('enter a element'))
        l.append(n)
    elif s==2:
        n=int(input('enter which element u delete'))
        if n in l:
            l.remove(n)
        else:
            print('invalid element')
    elif s==3:
        print('the list',l)
    elif s==4:
        break
    else:
        print('pls try again u r choosing wrong option')