#genarator is a function  which contains one or more yield statements
# it is also like return statement
#when ever u calling next function  in the generator function must be executed upto yield
def fun():
    n=1
    print('hi')
    yield n
    n=n+1
    print('bye')
    yield n
a=fun()
print(a)
print(next(a))
print(next(a))