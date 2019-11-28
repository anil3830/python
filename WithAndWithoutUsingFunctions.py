#with using max ,min functions
l=[1,2,3,4]
print('max of list',max(l))
print('min of list',min(l))
#no f elements in list by using len() function
l=[1,2,3,4,5,6]
print(len(l))
#without using len function
l=[1,2,3,6,5]
s=0
for i in l:
    if True:
       s=s+1
print(s)
#to print list in revers order
a=[1,2,3,4,5]
a.reverse()
print(a)
#with out using function
a=[1,2,3,4,5]
s=len(a)
print(a[-1:-s-1:-1])
#or
a=[1,2,3,4,5]
s=len(a)
n=[ ]
for i in range(s,0,-1):
        if True:
            n.append(i)
print(n)