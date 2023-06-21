from lib import *
import logging
# logging.basicConfig(level=logging.WARNING,
#                     format="%(asctime)s:%(levelname)s:%(message)s")
# filename="test.log",


if __name__ == "__main__":

    num_1 = 10
    num_2 = 5

    add_result = add(num_1, num_2)
    sub_result = substract(num_1, num_2)
    mul_result = multiply(num_1, num_2)
    div_result = devide(num_1, num_2)

    logging.info(f"Add: {num_1} + {num_2} = {add_result}")
    logging.info(f"Sub: {num_1} - {num_2} = {sub_result}")
    logging.info(f"Mul: {num_1} * {num_2} = {mul_result}")
    logging.info(f"Div: {num_1} / {num_2} = {div_result}")
