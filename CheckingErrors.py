#cheacking errors by using try, except , else, finally , key words
#ex multiple exception
'''try:
    a=int(input('enter a value'))
    d=int(input('enter  d value'))
    c=a/d
    print(c)
except ZeroDivisionError as x:
    print('the error is in',x)
##except TypeError as x:
    print('the error is in',x)
except NameError as x:
    print('the error is',x)
except ValueError as x:
    print('the error is in',x)
finally:
    print('thank you')'''
#
#
#single exception in multiple errors
n=int(input('enter any value'))
m=int(input('enter a number'))
try:
   c=n+m
   print(c)
except (ZeroDivisionError,NameError,TypeError,ValueError) as x:
     print('the error is in ',x)
finally:
    print('thank you')