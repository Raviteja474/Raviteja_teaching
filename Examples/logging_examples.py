import logging
import time

# logging is way of giving entry information.
# logging exactly does what print function
# debug<info<warning<error<critical


# level parameter specifies logging level
# filename will tell where we need to put the logs
# filemode  write(100 characters, if you write , it will erase all data and write from first) and
# append(contents will start from 101 line)


logging.basicConfig(level=logging.DEBUG, filename=r'C:\Users\ravit\Desktop\samsung_joining\log_'+str(time.time())+r'.txt', filemode='a')

a=b=2
c = a+2*b
logging.debug(f'C value is {c}')
if c>5:
    logging.debug("This is a wrong man!!, hAHAHAHAHAH")
print('This is a print message',time.time())
print("____________________________________________________________________")
logging.debug('This is a debug message {}'.format(time.time()))
logging.info('This is an info message{}'.format(time.time()))
logging.warning('This is a warning message {}'.format(time.time()))
logging.error('This is an error message {}'.format(time.time()))
logging.critical('This is a critical message {}'.format(time.time()))