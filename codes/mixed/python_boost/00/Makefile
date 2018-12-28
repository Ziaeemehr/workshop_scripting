# location of the Python header files

CXX = g++
CXXFLAG = -O2
PYTHON_VERSION = 2.7
PYTHON_INCLUDE = /usr/include/python$(PYTHON_VERSION)
 
# location of the Boost Python include files and library
 
BOOST_INC = /usr/include
BOOST_LIB = /usr/lib
 
# compile mesh classes
TARGET = hello_ext
 
$(TARGET).so: $(TARGET).o
	g++ -shared -Wl,--export-dynamic $(TARGET).o -L$(BOOST_LIB) -lboost_python -L/usr/lib/python$(PYTHON_VERSION)/config -lpython$(PYTHON_VERSION) -o $(TARGET).so
 
$(TARGET).o: $(TARGET).C
	g++ $(CXXFLAG) -I$(PYTHON_INCLUDE) -I$(BOOST_INC) -fPIC -c $(TARGET).C


clean:
	rm *.o *.so
	
.phoney: clean