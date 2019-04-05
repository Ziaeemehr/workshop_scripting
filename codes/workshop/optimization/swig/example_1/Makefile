CXX=g++
CXXFLAGS= -O2 -fPIC -c 
SWIGFLAGS = -c++ -python 


# location of the Python header files
PYTHON_VERSION = 2.7
PYTHON_INCLUDE = /usr/include/python$(PYTHON_VERSION)

TARGET = example
OBJS= $(TARGET).o $(TARGET)_wrap.o

_$(TARGET).so: $(OBJS)
	$(CXX) -shared  $(OBJS) -o _$(TARGET).so
 
$(TARGET)_wrap.o: $(TARGET)_wrap.cpp
	$(CXX) $(CXXFLAGS) $(TARGET)_wrap.cpp -I $(PYTHON_INCLUDE) 

$(TARGET).o: $(TARGET).cpp
	$(CXX) $(CXXFLAGS) $(TARGET).cpp 

$(TARGET)_wrap.cpp : $(TARGET).i 
	swig $(SWIGFLAGS) -o $(TARGET)_wrap.cpp $(TARGET).i 

clean :
	rm *.o  *.so $(TARGET)_wrap.cpp $(TARGET).py *.pyc 

.PHONEY : clean 




# swig -python example.i
# gcc -O2 -fPIC -c example.c
# gcc -O2 -fPIC -c example_wrap.c -I $(PYTHON_INCLUDE) 
# gcc -shared example.o example_wrap.o -o _example.so
