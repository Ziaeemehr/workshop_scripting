# gcc -c $(python2.7-config --cflags) 00.c
# gcc  00.o $(/usr/bin/python2.7-config --ldflags)

g++ -c $(python2.7-config --cflags) 00.cpp
gcc  00.o $(/usr/bin/python2.7-config --ldflags)

