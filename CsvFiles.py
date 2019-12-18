#it is usefull to separate the values
#this file 9is used to store each value separated by comas
#python provides csv module to handle thethese files
import csv
f=open('csv1.csv','w')
a=csv.writer(f)
a.writerow('welcome to hyd')
f.close()
#
#to store student marks in csv file
#writing
try:
    import csv
    with open('student info.csv','w+') as f:
         s=csv.writer(f)
         s.writerow(['kosmik tecchnologes'])
         n=int(input('how many number of students info u want'))
         for i in range(1,n+1):
              sname=input('enter s name')
              htnum=input('enter hallticket number')
              m1=int(input('enter m1 marks'))
              m2=int(input('enter m2 marks'))
              m3=int(input('enter m3 marks'))
              s.writerow([sname,htnum,m1,m2,m3])
         a=csv.reader(f)
         x=list(a)
         print(x)
except Exception as error:
    print('the error is',error)
'''#reading
import csv
with open('student info.csv','r') as a:
    s=csv.reader(a)
    c=list(s)
    for i in s:
        for j in i:
            print(j)
        print()
    a.close()
'''