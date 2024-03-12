import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(filename)s:%(levelno)s:%(message)s")
def average(given):
    total=0
    count=0

    for i in given:
         total += i
         count +=1


    if total is 0:
        logging.warning("Zero Average Detected")
    else:
        result = (total / count)
        logging.info(result)


