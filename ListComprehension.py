#creating list by using comprehensions
l=[ i for i in range(1,12)]
print(l)
print(type(l))
#
#list with squire
l=[ i*i for i in range(1,12)]
print(l)
#
#to creating list first characters of  each elements
l=['python','java','sql','html']
s=[ i[0] for i in l ]
print(s)
#or
l=['python','java','sql','html']
s=[]
for i in l:
    s.append(i[0])
print(s)
#
#common elements in list by using comprehension
l=[1,2,3,4,5]
s=[3,4,5,6,7]
c=[i for i in l if i in s ]
print('common elements',c)
