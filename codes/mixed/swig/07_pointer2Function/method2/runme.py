# https://stackoverflow.com/questions/22923696/how-to-wrap-a-c-function-which-takes-in-a-function-pointer-in-python-using-swi

import lib

# print type(lib.multiply)
# print type(lib.multiply_call)
# print repr(lib.multiply_call)
# print lib.multiply_call(2.0, 3.0)
print lib.multiply(2.0, 3.0)
print lib.myfun(2.0, 3.0, lib.multiply)