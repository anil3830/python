#built in methods in string
# finding lenth of string
l='python is high level language'
print(len(l))
#this function is used to convert character small to capital
#by using upper()
a='programs'
print(a.upper())
#this function is used to convert capital to small
#by usimg lower()
s='PYTHON'
print(s.lower())
#this function is use ful to check all characters in capital or not if yes returns true else false
#by using is upper()
n='PYTHON'
print(n.isupper())
#this function is use ful to check all characters in small or not if small returns true else false
#by using is lower()
m='projects'
print(m.islower())
#by using isdigit()
#this function is use ful to check all characters in the sting are digit or not isf yes returns true else false
z='a12bc'
print(z.isdigit())
z1='123'
print(z1.isdigit())
#by using capitalize()
#this function is use full to convert first character in given string in upper case
x='functions'
print(x.capitalize())
#by using swapcase() function
#this function is use full to convert lower case lattera into upper case and upper case latters into lower case
c='PYTHON'
v='projects'
print(c.swapcase())
print(v.swapcase())
#by using split() function
#this function use to split string in to list u can specify the separator by default separator is any blank space
e='good morning'
print(e.split())
print(e.split('g'))
# by using replace() function
#this function is use ful to replace the new string with old string
#you can specify the separator , if default separator  is in white space
p='python programs'
q='python is a high level language python is less code'
print(p.replace('python','java'))
print(q.replace('python','java',1))
#by using counting() function
#this is use full to number of times specified value appear in string
g='good morning'
print(g.count('o'))
#by using index() function
# it is use ful to find the index of spefied value
w='hello students'
print(w.index('s'))
print(w.index('students'))