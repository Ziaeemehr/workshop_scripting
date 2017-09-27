/*  example.h file */
#include <iostream>
#include <cstdio>
#include <vector>
#include <omp.h>


class my_class 
{
    private:    
        int N;
    public:
        my_class(){ }
        std::vector<double> half(const std::vector<double>& ); 
};
