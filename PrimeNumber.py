n=int(input('enter any number'))
i=1
x=0

while n!=0:
    if n<i:
        break
    if n%i==0:
        x=x+1
    i=i+1
if x==2:
    print('given number is prime')
else:
    print('given no is not prime')

