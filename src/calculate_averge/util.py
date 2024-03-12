import logging
logging.basicConfig(filename="log.test", level=logging.DEBUG, format="%(asctime)s:%(filename)s:%(levelno)s:%(message)s")
def average(given):
    total=0
    count=0

    for i in given:
        total += i
        count +=1
    result = (total/count)
    logging.debug(result)


