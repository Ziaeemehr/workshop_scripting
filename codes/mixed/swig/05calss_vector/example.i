%module example

%{
#define SWIG_FILE_WITH_INIT
#include "example.h"
%}

%include "std_vector.i"

namespace std {
    %template(DoubleVector)  vector<double>;
}


%include "example.h"
