# 1 syntax error  like typing mistakes,incorrect arguments
#eol  end of th
'''x='good morning
print(x)
#eof end of the file
p;print('goodmorning
 #
#2  logical errors or sematric
#program might run without syntax,run time error but still do wrong out put
#ex addition of numbers
z=int(input('enter a number'))
a=int(input('enter a number'))
c=a*z
print(c)
#like this type

#run time  error
# programe run without syntax,logical errors but while running the program it returns error is called run time error
#so many run time errors is there
# 1 zero division error
a=19
b=0
c=a/b
print(c)
#
#2 name error
while i<n:
    print(i)
    i=i+1
#
#3 type error
a='asd'
b=2
c=a+b
print(c)
#
#4 index error
a=[1,2,3,4]
print(a[2])
print(a[22])
#
#5 value error
a=[1,2,3,4]
print(a.index(1))
print(a.index(22))
#
#key error
s={1,2,3,4}
print(s)
s.remove(2)
print(s)
s.remove(22)
print(s)'''
#
#attribute error
s={1,2,3}
print(s)
s.delete(3)
print(s)