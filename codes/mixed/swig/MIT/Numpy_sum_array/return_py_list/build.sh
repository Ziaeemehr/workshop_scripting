swig -python -c++ -o get_rand_list_wrap.cpp get_rand_list.i
gcc -c get_rand_list.cpp -o get_rand_list.o -fpic -std=c++0x
gcc -I/usr/include/python2.7 -c get_rand_list_wrap.cpp -o get_rand_list_wrap.o -fpic -std=c++0x
g++ get_rand_list_wrap.o get_rand_list.o -o _get_rand_list.so -shared -Wl,-soname,_get_rand_list.so
