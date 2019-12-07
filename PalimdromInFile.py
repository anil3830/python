#revers file
try:
    with open('ts.t','r') as a:
         with open('text.text', 'w') as b:
             n=" "
             s=a.read()
             for i in s:
                 n=i+n
             print('revers file is ',n)
             b.write(n)
except Exception as error:
    print('the error is',error)

#plindron in file
try:
 with open('ts.t','r') as a:
     with open('palindrom.text','w') as b:
         y=' '
         x=' '
         s=a.read()
         if x==' ':
             y=s.split()
             for i in y:
                 p=''
                 for j in i:
                     p=j+p
                 if i==p:
                     print('the palindrom is',p)
except Exception as error:
    print('the error is in ',error)


