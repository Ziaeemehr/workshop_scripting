swig -python -c++ -o saxpy_wrap.cpp saxpy.i
gcc -c saxpy.cpp -o saxpy.o -fpic -std=c++0x
gcc -I/usr/include/python2.7 -c saxpy_wrap.cpp -o saxpy_wrap.o -fpic -std=c++0x
g++ saxpy_wrap.o saxpy.o -o _saxpy.so -shared -Wl,-soname,_saxpy.so