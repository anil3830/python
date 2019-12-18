#public attribute or variable
#public varible can access anywhate inside or outside of the class
import  logging
import LoggersEx1
logger=logging.getLogger(__name__)
class ex:
    a=10
    c=2
    def print(self):
        logger.info('%s %s',ex.a,ex.c)

s1=ex()
s1.print()
print(s1.a)
print(s1.c)
#
#protected variables
#in this variable can access anyehar in class but out side of the class access only chaild class
class ex1:
   _a=20
   _c=2
   def print(self):
        logger.info('%s %s',ex1._a,ex1._c)

s1=ex1()
s1.print()
print(ex1._a)
print(ex1._c)
#s1.print(ex1._a)
#s1.print(ex1._c)
#private variables
#in this attribute access only with in the class con`t access outside of class
class ex2:
   try:
       __a=20
       __c=3
       def print(self):
           logger.info('%s %s',ex2.__a,ex2.__c)
   except Exception as error:
       logger.error('%s the error is',error)
s1=ex2()
s1.print()
#print(ex2.__a)
#print(ex2.__c)