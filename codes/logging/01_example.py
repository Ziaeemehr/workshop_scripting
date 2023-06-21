# https://docs.python.org/3/library/logging.html
# https://www.youtube.com/watch?v=-ARI4Cz-awo

# DEBUG     : Detailed information, of interest only when diagnosing a problem.
# INFO      : Confirmation that everything is working as expected.
# WARNING   : An indication that something unexpected has happened, or the possibility of a problem in the near future (eg "low disk space"). The software still works normally.
# ERROR     : Due to a more serious problem, the software was unable to complete a task.
# CRITICAL  : A serious error, indicating that the program itself might be unable to continue running.

# logging.info()(or logging.debug()for very detailed output for diagnostic purposes)
# warnings.warn()in the library code if the problem is preventable and the client application needs to be modified to eliminate this warning
# logging.warning()if the client application cannot do anything to correct the situation but the event should still be noted
# logging.error(), logging.exception()or logging.critical(), at best, depending on the specific error and area of ​​application

import logging
logging.basicConfig(level=logging.ERROR,
                    format="%(asctime)s:%(levelname)s:%(message)s")
# filename="test.log",

# print(logging.DEBUG) # 10

def add(x, y):
    return x+y


def substract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def devide(x, y):
    return x/y


num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
sub_result = substract(num_1, num_2)
mul_result = multiply(num_1, num_2)
div_result = devide(num_1, num_2)

logging.warning(f"Add: {num_1} + {num_2} = {add_result}")
logging.warning(f"Sub: {num_1} - {num_2} = {sub_result}")
logging.warning(f"Mul: {num_1} * {num_2} = {mul_result}")
logging.warning(f"Div: {num_1} / {num_2} = {div_result}")
