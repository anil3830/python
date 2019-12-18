#creating default constructors
#creating object without parameters is called default constructors
#ex1
import logging
import  LoggersEx1
logger=logging.getLogger(__name__)
logger.info('121111')
class test:
    try:
        def  __init__(self):
            #print('default')
             logger.info('it is a default function')
    except Exception as error:
           logger.error('%s error is in',error)
t=test()
#
#to count no of objects create in class
class  find:
    try:
       count=0
       def __init__(self):
           find.count=find.count+1
       def print(self):
           logger.info('%s no of objects created',find.count)
    except Exception as error:
        logger.error('%s erroe is',error)
a=find()
s=find()
m=find()
m.print()