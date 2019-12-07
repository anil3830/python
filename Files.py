#1 text file
#by using w mode means --it is useful to writing purpose
# to print typess of course names
f=open('C:/Users/gopi/Desktop/Files/file2.text','w')
f.write('python\n')
f.write('java\n')
f.write('c\n')
f.close()
#
f=open('file1.text','w')
f.write('kosmik\n')
f.write('instute\n')
f.close()
#
#by using 'a'mode---means append
#adding new data in to file
f=open('file1.text','a')
f.write('html\n')
f.write('sql\n')
f.close()
#
#using writelines() function
# it is useful to multi lines of text
x=open('file2.text','w')
x.writelines('python\njava\nc\n')
x.close()
#
#by using x  mode
#it is usefull the file exist or not  if already exist it shows file exist error otherwise to create new file
try:
   x=open('file1.text','x')
   x.wrie('python\n')
   x.write('java')
except Exception as error:
    print('error is',error)