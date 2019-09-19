#include <iostream>
#include <stdio.h>
#include <vector>
#include <cmath>

using std::cout;
using std::endl;
using std::vector;

//--------------------------------------------------------------
double pdf(const double x)
{
    return (1.0 / sqrt(2 * M_PI) * exp(-0.5 * x * x));
}
//--------------------------------------------------------------
double cdf(const double x)
{
    return 0.5 * (1.0 + erf(x / sqrt(2.0)));
}
//--------------------------------------------------------------
template <typename T>
std::vector<double> linspace(
    T start_in,
    T end_in,
    long unsigned num_in)
{

    std::vector<double> linspaced;

    double start = static_cast<double>(start_in);
    double end = static_cast<double>(end_in);
    double num = static_cast<double>(num_in);

    if (num == 0)
    {
        return linspaced;
    }
    if (num == 1)
    {
        linspaced.push_back(start);
        return linspaced;
    }

    double delta = (end - start) / (num - 1);

    for (int i = 0; i < num - 1; ++i)
    {
        linspaced.push_back(start + delta * i);
    }
    linspaced.push_back(end); // I want to ensure that start and end
                              // are exactly the same as the input

    return linspaced;
}
//--------------------------------------------------------------
double skewd_normal_distribution(
    const double x,
    const double loc,
    const double scale,
    const double skew)
{
    double t = (x - loc) / scale;
    return (2.0 / scale * pdf(t) * cdf(skew * t));
}
