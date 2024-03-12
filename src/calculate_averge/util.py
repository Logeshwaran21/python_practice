import logging
def average(given):
    total=0
    count=0

    for i in given:
        total += i
        count +=1
    result = (total/count)
    logging.warning(result)


