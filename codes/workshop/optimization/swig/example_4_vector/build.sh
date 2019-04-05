swig -c++ -python -shadow example.i
g++  -std=c++11 -O2 -fPIC -fopenmp -c example.cpp 
g++  -std=c++11 -O2 -fPIC -c example_wrap.cxx -I /usr/include/python2.7 
g++  -shared example_wrap.o example.o -o _example.so 
