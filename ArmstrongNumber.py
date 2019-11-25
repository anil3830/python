n=int(input('enter a number'))
l=n
x=len(str(n))
r=0
for i in range(1,n):
    d=n%10
    r=r+d**x
    n=n//10
    if n==0:
        break
if r==l:
    print('given number is armstrong')
else:
    print('given number is not armstrong')