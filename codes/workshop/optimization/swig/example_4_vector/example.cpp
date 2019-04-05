#include "example.h"

std::vector<double> my_class::half(const std::vector<double>& v) {
    std::vector<double> w(v);
    #pragma omp parallel for
    for (unsigned int i=0; i<w.size(); i++)
        w[i] /= 2.0;
    return w;
}
