#by using two for loops
l=[1,2,3,4,5]
m=[3,4,5,6,7]
n=[]
for i in l:
    for j in m:
        if i==j:
            n.append(i)
print('common elements is',n)

#by using onebfor loop
l=[1,2,3,4,5]
m=[3,4,5,6,7]
k=[]
for i in l:
    if i in m:
        k.append(i)
print('common elements is',k)
#by using string values
l=['ram','ravi','raju']
l2=['rock','roman','ram']
l3=[]
for i in l:
    if i in l2:
        l3.append(i)
print('common elements is',l3)


#find sum of list by using sum() funstion
l=[1,2,3,4,5]
print('sum of elements',sum(l))
#with out using sum function
l=[1,2,3,4,5]
m=0
for i in l:
    m=m+i
print('sum of list is',m)