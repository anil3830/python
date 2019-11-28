d={1:'python',2:'java',3:'c'}
print(d)
print(len(d))
print(max(d))
print(min(d))
print(sum(d))
#by using key() function
d={1:'python',2:'java',3:'c'}
print(d)
#print(d.keys())(not using)
for i in d.keys():
    print(i)
#by using values() function
d={1:'python',2:'java',3:'c'}
print(d)
for i in d.values():
    print(i)
# by using iteams() function
d={1:'python',2:'java',3:'c'}
print(d)
for i in d.items():
    print(i)
for i,j in d.items():
    print(i,"---",j)