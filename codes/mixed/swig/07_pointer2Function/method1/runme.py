# https://stackoverflow.com/questions/22923696/how-to-wrap-a-c-function-which-takes-in-a-function-pointer-in-python-using-swi

import lib

# print type(lib.f)
# print repr(lib.f)
# print type(lib.make_fptr())
# print repr(lib.make_fptr())


# <type 'builtin_function_or_method'>
# <built-in function f>
# <type 'SwigPyObject'>
# <Swig Object of type 'fptr_t' at 0x7f0ac7a78660>

# solution 1

multiply = lib.make_fptr()
print lib.myfun(2.0, 3.0, multiply)
