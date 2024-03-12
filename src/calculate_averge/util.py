import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(filename)s:%(levelno)s:%(message)s")
def average(given):
    total = 0
    count = 0
    for i in given:
         total += i
         count +=1

    if total is 0:
        result_1= "Zero Average Detected"
        logging.warning(result_1)
        return result_1
    else:
        result = (total / count)
        rounded_result= round(result,2)
        logging.info(f"Average: {rounded_result:.2f}")
        return rounded_result


