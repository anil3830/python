# class--a collection of variables(data members) and functions(methods) is called class
#to creating class only variables
import logging
import LoggersEx1
class Add:
    logger=logging.getLogger(__name__)
    try:
        a=4
        d=3
        logger.info(a+d)
    except Exception as error:
        logger.error("the error is",error)
#'''
#to creating class only methods
import logging
import LoggersEx1
#class file:
logger=logging.getLogger(__name__)
logger.info("============issii")
class file:
    try:
        def m2():
            logger.info('method 1 is here')
        def m1():
            logger.info('method 2 is here')
    except Exception as a:
         logger.error('the error is in ',a)

file.m2()
file.m1()
#

#to create class with variable and class
import logging
import LoggersEx1
class rectangle:
    logger=logging.getLogger(__name__)
    try:
        def read():
            rectangle.l=int(input('enter length'))
            rectangle.b=int(input('enter breath'))
        def find():
            rectangle.area=rectangle.l*rectangle.b
        def display():
            logger.info('%s length ',rectangle.l)
            logger.debug('%s breath',rectangle.b)
            logger.info('%s area',rectangle.area)
    except Exception as a:
            logger.error('the error is',a)

rectangle.read()
rectangle.find()
rectangle.display()