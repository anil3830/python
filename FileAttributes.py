x=open('file1.text','a')
#by using name it returns the name of the file
print('filee1.text',x.name)
#by using 'mode' it is use full to know the file mode
print('file1.text',x.mode)
#by using 'writable()' if file is writable it returns True otherwise it returns false
print('file1.text',x.writable())
# by using 'readable()' if it is readable it returns true else returns false
print('file.text',x.readable())
# by using 'closed'it is use fullto check fileis closed or not if closed it returns true else false
print('file1.text',x.closed)
x.close()
print('file1.text',x.closed)
print('---------')
#ex
a=open('text.text','w')
a.write('ravi\n')
a.write('raju\n')
a.close()
t=open('text.text','r')
print('text.text',t.name)
print('text.text',t.mode)
print('text.text',t.writable())
print('text.text',t.readable())
t.close()
print('text.text',t.closed)