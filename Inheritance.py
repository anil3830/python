#single inheritance
# deriving class is derived by only one base class is called single inheritance
import logging
import LoggersEx1
logger=logging.getLogger()
class person():
    def age(self):
        logger.info('age----65')
class person1(person):
    def height(self):
        logger.info('height ---6')
p=person1()
p.age()
p.height()

#multilevel inheritance
#drived class drived from another drived class is called multilevel inheritance
class animal:
    def bark(self):
        logger.info('it barks-----')
class dog(animal):
    def bite(self):
        logger.info('it bites-----')
class snoopy(dog):
    def eat(self):
        logger.info("it is eating -------")

d=snoopy()
d.bark()
d.bite()
d.eat()
#
#multiple inheritance
# a derived class derived from more then one base class is called multiple inheritance
class a:
    def add(self,x,y):
        z=x+y
        logger. debug("%s ",z)
class b:
    def sub(self,x,y):
        z=x-y
        logger.info("%s",z)
class c(a,b):
    def mul(self,x,y):
        z=x*y
        logger.info("%s",z)
s=c()
s.add(2,4)
s.sub(3,5)
s.mul(4,6)
#
# hierarical inheritance
# only one base clss and number of derived class or sub class is called hierarical inheritance
class a:
    def m1(self):
        logger.info("----m1")
class b(a):
    def m2(self):
        logger.info("----m2")
class c(a):
    def m3(self):
        logger.debug("-----m3")
b1=b()
b1.m1()
b1.m2()
c1=c()
c1.m1()
c1.m3()
#
#hybrid inheritance
# it is a combination of  single,multilevel,multiple,hierarical inheritance
class a:
    def m1(self):
        logger.debug('------m1---')
class b(a):
    def m2(self):
        logger.info('-----m2-----')
class c(a):
    def m3(self):
        logger.info('---m3---')
class d(b,c):
    def m4(self):
        logger.debug('--m4---')
e=d()
e.m1()
e.m2()
e.m3()
e.m4()