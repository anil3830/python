#by using Rising  keyword
#to rise exception
'''n=int(input('enter starting point of list'))
m=int(input('enter ending point of list'))
l=list(range(n,m))
for i in l:
    if i<5:
        raise Exception(' sorry,bellow the five , values does not taken')
    print(i)
else:
    print('thank you')
#
#tex
x=int(input('enter a value'))
if x>3:
    raise Exception('x should not exced 3 the value of x is was: ()',format(x))
else:
    print('the value of x is',x)
#
#ex 2'''
n=int(input('enter a number'))
try:
    if n<=0:
         raise Exception('zero,below the zero values are does not taken')
    else:
         print('the value of n is',n)
except Exception as a:
    print('the error is in',a)
finally:
    print("------")

print("========")

