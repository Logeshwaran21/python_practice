import logging

from util import factorial
logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(filename)s:%(levelname)s:%(message)s")
num = int(input("Enter the value: "))
result = factorial(num)
logging.debug(result)