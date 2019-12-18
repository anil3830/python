# the instance of class is called class
import  logging
import LoggersEx1
logger = logging.getLogger(__name__)
#creating object
class ex:
    c=3
    d=4
s1=ex()
print(type(s1))
logger.info("in test")
print(s1.c)
print(s1.d)
#cl
#creating rectangle objects
class rectangle:
    def read(x):
        print(type(x))
        x.l=int(input('enter length'))
        logger.info("===============Gopi")
        x.b=int(input('enter breath'))
    def find(x):
        x.area=x.l*x.b
    def display(x):
        print('length',x.l)
        print('breath',x.b)
        print('area',x.area)
def main():
   r=rectangle()
   r.read()
   r.find()
   r.display()
#or
   r2=rectangle()
   r2.read()
   r2.find()
   r2.display()
main()
##
# by using logging , try ,except
import logging
class student():
    logger=logging.getLogger(__name__)
    try:
        def read(x):
            x.Name=input('enter name')
            x.m1=int(input('enter m1 marks'))
            x.m2=int(input('enter m2 marks'))
        def find(x):
            x.total=x.m1+x.m2
            x.avg=x.total/2
        def display(x):
            logger.info(" %s =total", x.total)
            logger.info("%s =avg",x.avg)
    except Exception as e:
         logger.error('the error is')
s1=student()
s1.read()
s1.find()
s1.display()