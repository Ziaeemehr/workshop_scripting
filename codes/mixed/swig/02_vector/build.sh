swig -c++ -python example.i
g++  -O2 -fPIC -c example_wrap.cxx -I /usr/include/python2.7 
# g++  -O2 -fPIC -c example_wrap.cxx -I /usr/include/python3.6 
g++  -shared  example_wrap.o -o _example.so
