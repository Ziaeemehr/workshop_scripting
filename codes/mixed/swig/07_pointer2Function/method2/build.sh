swig -c++ -python lib.i
g++  -O2 -fPIC -c lib_wrap.cxx -I /usr/include/python2.7 
# g++  -O2 -fPIC -c lib_wrap.cxx -I /usr/include/python3.6 
g++  -shared  lib_wrap.o -o _lib.so
