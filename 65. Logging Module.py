# ---------------------------Logging module--------------------
# for tracking logs and recording logs.
# for storing every activity is called logging

# logging levels:
# 6 levels of priority
#1. Critical => 50 => Most critical
#2. Error => 40 => Less critical
#3. Warning => 30 => Alert the programmer
#4. INFO => 20 => information
#5. DEBUG => 10 => Debugging
#6. NOTSET  => 0 => Logging level not set
# By default only warning and critical will show.
# how to implement logging:

#a). name of the file
#b). level messages

import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING)
print('Python logging demo')
logging.debug('Debugging Messages')
logging.info('Info Messages')
logging.warning('Warning Messages')
logging.error('Error Messages')
logging.critical('Critical Messages')

logging.info('A new request came')
try:
    x=int(input('Enter first number:'))
    y=int(input('Enter second number:'))
    print(x/y)
except ZeroDivisionError as msg:
    print('Can''t Divide with Zero')
    logging.exception(msg)
except ValueError as msg:
    print('Value error')
    logging.exception(msg)
    logging.info('Request processing completed')

#logging.Text



