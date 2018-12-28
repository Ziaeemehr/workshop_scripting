# CC = g++
# PYLIBPATH = $(shell python-config --exec-prefix)/lib
# LIB = -L$(PYLIBPATH) $(shell python-config --libs) -lboost_python
# OPTS = $(shell python-config --include) -O2

# default: zoo.so
# 	@python ./visit_zoo.py

# zoo.so: zoo.o
# 	$(CC) $(LIB) -Wl,-rpath,$(PYLIBPATH) -shared $< -o $@

# zoo.o: zoo.cpp Makefile
# 	$(CC) $(OPTS) -c $< -o $@

# clean:
# 	rm -rf *.so *.o

# .PHONY: default clean



# location of the Python header files
 
PYTHON_VERSION = 2.7
PYTHON_INCLUDE = /usr/include/python$(PYTHON_VERSION)
 
# location of the Boost Python include files and library
 
BOOST_INC = /usr/include
BOOST_LIB = /usr/lib
 
# compile mesh classes
TARGET = zoo
 
$(TARGET).so: $(TARGET).o
	g++ -O2 -shared -Wl,--export-dynamic $(TARGET).o -L$(BOOST_LIB) -lboost_python -L/usr/lib/python$(PYTHON_VERSION)/config -lpython$(PYTHON_VERSION) -o $(TARGET).so
 
$(TARGET).o: $(TARGET).cpp
	g++ -I$(PYTHON_INCLUDE) -I$(BOOST_INC) -fPIC -c $(TARGET).cpp

clean :
	rm *.o *.so
.phoney: clean



# g++ -shared -Wl,--export-dynamic $(TARGET).o -L$(BOOST_LIB) -lboost_python-$(PYTHON_VERSION) -L/usr/lib/python$(PYTHON_VERSION)/config -lpython$(PYTHON_VERSION) -o $(TARGET).so