%module example

%{
#define SWIG_FILE_WITH_INIT
#include "example.h"
%}

%include "std_vector.i"
%include <complex.i>
%include <std_complex.i>
namespace std {
    %template(DoubleVector)  vector<double>;
    %template(ComplexVector) vector<std::complex<double> >;
    %template(ComplexVector2) vector<vector<std::complex<double> > >;
}


%include "example.h"
