#  number of argumants is equalto formal argumants
# position is importent
# positional argumants: in functions
# ex: equal arguments
def mul(a,b):
    m=a*b
    m=a*b
    return m
c=int(input('enter c value'))
d=int(input('enter d value'))
v=mul(c,d)
print(v)
#ex : positions
def d(y,x):
    print('mame of persion',y)
    print('age of persion',x)
d('ramu',22)
#
#keyword argument
#here position is not impartent
#function values passing rthrough arguments are assigned to parameters irrespective of its position
#when u call the function it supply the values
def names(a,b):
    print(a + b +  ' are friends' )
names('ramu ','sonu')
names(a='ramu ',b='sonu')
#
#default argument
#here numbers and position is not impartent
#by using '='operator
def details(a=20,n='raju',m=4):
    print('age  of persion',a)
    print('name of the persion',n)
details( )
details('ravi',23)

#
#variable length arguments
#by using '*' operator
#here number of arguments and position is not impartent
def calculate(*x):
    sum=0
    print(x)
    print(type(x))
    for i in x:
        sum=sum+i
    print('sum of elements',sum)
calculate(1,2,3,-1)
calculate( )
#
#keyword variable length arguments
#by using'**'op
#here also number of srguments and position is not importent
def declare(**x):
    print(x)
    print(type(x))
declare(a=1,b=3,c=5,h=4)
declare( )