# class--a collection of variables(data members) and functions(methods) is called class
#to creating class only variables
'''import logging
class Add:
    logger=logging.getLogger(__name__)
    try:
        a=4
        d=3
        logger.info(a+d)
    except Exception as error:
        logger.warning("the error is",error)
#'''
#to creating class only methods
import logging
#class file:
logger=logging.getLogger(__name__)
class file:
    try:
        def m2(x):
            logger.info('method 1 is here')
        def m1(x):
            logger.info('method 2 is here')
    except Exception as a:
         logger.error('the error is in ',a)

file.m2()
file.m1()
#

#to create class with variable and class
import logging
class rectangle:
    logger=logging.getLogger(__name__)
    try:
        def read(x):
            x.l=int(input('enter length'))
            x.b=int(input('enter breath'))
        def find(x):
            x.area=x.l*x.b
        def display(x):
            logger.info('length =',x.l)
            logger.debug('breath=',x.b)
            logger.info('area=',x.area)
     except Exception as a:
            logger.error('the error is',a)

rectangle.read()
rectangle.find()
rectangle.display()