#creating set with elements in set comprehension
s={i for i in range(1,11)}
print(s)
#
#common elements in set
s={1,2,3,4,5}
s1={2,4,6,8,1}
s3={ i for i in s if i in s1}
print(s3)
#
#print how many diffrent vowels in present word
v={'a','e','i','o','u'}
n=input('enter any word')
s={ i[0] for i in v if i in n}
print(s)