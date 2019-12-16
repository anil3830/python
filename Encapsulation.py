#encapsulation
import logging
import LoggersEx1
logger=logging.getLogger(__name__)
class Emp:
    def __init__(self,x,y):
        self.__eName=x
        self.__eSal=y
    def print(self):
        logger.info('%s',self.__eName)
        logger.info("%s",self.__eSal)
e=Emp('fdfg',4321)
e.print()
s=Emp('jgty',6565)
s.print()