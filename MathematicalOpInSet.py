#union() or |
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a.union(b)
d=b.union(a)
e=a|b
f=b|a
print(c)
print(d)
print(e)
print(f)
#intersection()  or &

a={1,2,3,4}
b={3,4,5,6}
c=a.intersection(b)
d=b.intersection(a)
e=a&b
f=b&a
print(c)
print(d)
print(e)
print(f)

#intersection_update()
a={1,2,3,4}
b={3,4,5,6}
c=a.intersection_update(b)
print("a",a)
print(b)

#diffrence()  or -
a={1,2,3,4}
b={3,4,5,6}
c=a.difference(b)
d=b-a
print(d)
print(c)
#symetric diffrence() or ^
a={1,2,3,4}
b={3,4,5,6}
c=a.symmetric_difference(b)
print(c)

#example for all above operators
a={"ram",1,"sita",2}
b={1,2,"lakshman",3,"hanuman",4}
print(a|b)
print(a&b)
print(a-b)
print(a^b)
print(a.intersection_update(b))
print(a)
print(b)