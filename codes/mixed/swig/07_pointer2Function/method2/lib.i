%module lib

%{
#include "lib.hpp"
%}
// %constant double multiply(double, double);
// %rename(multiply_call) multiply;
// %ignore multiply;

%callback("%s_cb");
double multiply(double, double);
%nocallback;
%include "lib.hpp"