/*  example.h file */
#include <iostream>
#include <cstdio>
#include <Eigen/Dense>

using Eigen::MatrixXd;


class my_class 
{
    private:    
        int N;
    public:
        my_class(){ }
        void printMatrix();
        MatrixXd getMatrix();
};
