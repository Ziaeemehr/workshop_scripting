swig -python -c++ -o sum_array_wrap.cpp sum_array.i
g++ -c sum_array.cpp -o sum_array.o -fpic -std=c++0x
g++ -I/usr/include/python2.7 -I /usr/local/lib/python2.7/dist-packages/numpy/core/include/ -c sum_array_wrap.cpp -o sum_array.o -fpic -std=c++0x
g++ sum_array_wrap.o sum_array.o -o _sum_array.so -shared -Wl,-soname,_sum_array



# export CFLAGS="-I /usr/local/lib/python2.7/dist-packages/numpy/core/include/ $CFLAGS"
# PYTHON_INCLUDE := /usr/include/python2.7 \
#         /usr/local/lib/python2.7/dist-packages/numpy/core/include
