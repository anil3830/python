# by using setdefault()
d={1:'python',2:'java',3:'c'}
print(d)
d.setdefault(4,'sql')
d.setdefault(5,'html')
print(d)
# by using popitem()
d={1:'python',2:'java',3:'c'}
print(d)
d.popitem()
print(d)

#by using pop() function
d={1:'python',2:'java',3:'c'}
print(d)
d.pop(1)
d.pop(2)
print(d)

#using get() function
d={1:'python',2:'java',3:'c'}
print(d)
print(d.get(2))
print(d.get(3))

