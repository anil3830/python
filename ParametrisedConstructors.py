#to create a object with parameters is called parametrised constructors
#it initialise the class variables
#ex
import logging
import LoggersEx1
logger=logging.getLogger(__name__)
class os:
    try:
        def __init__(self,x,t):
             self.osName=x
             self.osInterduceyear=t
        def print(self):
            logger.info('%s =os Name',self.osName)
            logger.debug('%s =os intraduced year',self.osInterduceyear)
    except Exception as error:
           logger.error('%s the error is in ',error)
a=os("android",1997)
a.print()
#
# ex 2
class bank:
    def __init__(self,x,y,z):
        self.acNumber=x
        self.personName=y
        self.balance=z
    def print(self):
        logger.info('%s acount number is',self.acNumber)
        logger.info("%s acount holder name",self.personName)
        logger.info('%s balance',self.balance)

n=bank(111111,'dfsefrw',940494.44)
n.print()
