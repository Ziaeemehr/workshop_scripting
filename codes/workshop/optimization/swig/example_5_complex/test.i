%module test
%{
	#include <complex>
%}

%include <complex.i>

%inline %{
	double complex test (double complex X) {
		return X;
	}
%}