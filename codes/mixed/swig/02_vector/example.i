/* File : example.i */
%module example

%{
#include "example.h"
%}

%include "std_vector.i"
/* instantiate the required template specializations */
namespace std {
    %template(IntVector)    vector<int>;
    %template(DoubleVector) vector<double>;
    %template(IntVector2)   vector<vector<int>>;
}

/* Let's just grab the original header file here */
%include "example.h"

