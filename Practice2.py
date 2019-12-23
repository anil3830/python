import logging
import LoggerEx1
logger=logging.getloggerconfig(__name__)
try:
   class dog:
        def eat(self,*x):#over ridind
            for i in len(x):     #for loop using
                if i!=0: # if condition
                    logger.info('%S',i)
                else:
                    logger.info('------')# loggers using
            logger.info("%s",i)
        def behave(self,_a,__b,c):# public private protct variables
            self._a='harsh'
            self.__b='rood'
            self.c='friendly'
            logger.info('dog behave %s %s %s',self.c,self,_a,self.__b)
   class bird(dog):    #    in heritance
        def eat(self,*r):
            super().eat()
            logger.info('birds eat %s %s',self.r)
   t=bird()            # object creation
   t.eat('inserts','food')  #
   t.behave()
   logger.info('%s',t._a,t.__b,t.c)
except Exception as error:            #try except functions
    logger.error('the error is %s',errror)