import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(filename)s:%(levelno)s:%(message)s")

def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        result =num* factorial(num-1)
        return result
    logging.debug(result)