CXX=g++
CXXFLAGS  = -O2 -fPIC -c 
SWIGFLAGS = -c++ -python -shadow  

# location of the Python header files
PYTHON_VERSION = 2.7
PYTHON_INCLUDE = /usr/include/python$(PYTHON_VERSION)

TARGET = number
OBJS= $(TARGET).o $(TARGET)_wrap.o

_$(TARGET).so: $(OBJS)
	$(CXX) -shared  $(OBJS) -o _$(TARGET).so
 
$(TARGET)_wrap.o: $(TARGET)_wrap.cxx
	$(CXX) $(CXXFLAGS) $(TARGET)_wrap.cxx -I $(PYTHON_INCLUDE) 

$(TARGET).o: $(TARGET).cxx
	$(CXX) $(CXXFLAGS) $(TARGET).cxx

$(TARGET)_wrap.cxx : $(TARGET).i 
	swig $(SWIGFLAGS) $(TARGET).i 

clean :
	rm *.o  *.so $(TARGET)_wrap.cxx $(TARGET).py *.pyc 

.PHONEY : clean 




# swig -c++ -python  -shadow number.i
# g++ -O2 -fPIC -c number.cxx
# g++ -O2 -fPIC -c number_wrap.cxx -I /usr/include/python2.7 
# g++ -shared number.o number_wrap.o -o _number.so