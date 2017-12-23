/*  example.h file */
#include <iostream>
#include <cstdio>
#include <vector>
#include <omp.h>
#include <complex>

typedef std::complex<double> Complex;
typedef std::vector<Complex> dim1C;
typedef std::vector<std::vector<Complex> > dim2C;

class my_class
{
    private:    
        int N;
        Complex com1;
        std::vector<Complex> comV;
    public:
        my_class(){ }
        void set_value(Complex a, const std::vector<Complex> );
        std::vector<Complex> half(const std::vector<Complex>& );
        dim2C half2(const dim1C& );
        void print_value();
};
