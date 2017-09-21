CXX=g++
CXXFLAGS= -O2 -fPIC -c 

# location of the Python header files
PYTHON_VERSION = 2.7
PYTHON_INCLUDE = /usr/include/python$(PYTHON_VERSION)

TARGET = example
OBJS= $(TARGET).o $(TARGET)_wrap.o

_$(TARGET).so: $(OBJS)
	$(CXX) -shared  $(OBJS) -o _$(TARGET).so
 
$(TARGET)_wrap.o: $(TARGET)_wrap.c
	$(CXX) $(CXXFLAGS) $(TARGET)_wrap.c -I $(PYTHON_INCLUDE) 

$(TARGET).o: $(TARGET).c
	$(CXX) $(CXXFLAGS) $(TARGET).c 

$(TARGET)_wrap.c : $(TARGET).i 
	swig -python $(TARGET).i 

clean :
	rm *.o  *.so $(TARGET)_wrap.c $(TARGET).py  

.PHONEY : clean 




# swig -python example.i
# gcc -O2 -fPIC -c example.c
# gcc -O2 -fPIC -c example_wrap.c -I $(PYTHON_INCLUDE) 
# gcc -shared example.o example_wrap.o -o _example.so