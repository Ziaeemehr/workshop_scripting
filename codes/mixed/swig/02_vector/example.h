/* File : example.h */

#include <vector>
#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <assert.h>

// typedef std::complex<double> Complex;

//-----------------------------------------------------------------//
double average(std::vector<int> v) {
    return std::accumulate(v.begin(),v.end(),0.0)/v.size();
}

//-----------------------------------------------------------------//
std::vector<double> half(const std::vector<double>& v) {
    std::vector<double> w(v);
    for (unsigned int i=0; i<w.size(); i++)
        w[i] /= 2.0;
    return w;
}
//-----------------------------------------------------------------//

void halve_in_place(std::vector<double>& v) {
    // would you believe this is the same as the above?
    std::transform(v.begin(),v.end(),v.begin(),
                   std::bind2nd(std::divides<double>(),2.0));
}
//-----------------------------------------------------------------//
std::vector<std::vector<int>> reshape_2d(const std::vector<int> &x1d, const int N)
{
    std::vector<std::vector<int>> x2d(N, std::vector<int>(N));

    for (int i = 0; i < x1d.size(); i++)
    {
        int row = i / N;
        int col = i % N;
        x2d[row][col] = x1d[i];
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            std::cout << x2d[i][j] << "\t";
        }
        std::cout << "\n";
    }

    return x2d;
}
//-----------------------------------------------------------------//
// std::pair<double, double> averagePair(const std::vector<int> &v1,
//                                       const std::vector<int> &v2)
// {
//     assert(v1.size() == v2.size());
//     int N = v1.size();
//     std::vector<std::pair<int, int>> V(N);
//     for (int i = 0; i < v1.size(); ++i)
//     {
//         V[i].first = v1[i];
//         V[i].second = v2[i];
//     }

//     double first = 0.0;
//     double second = 0.0;
//     for (auto i : V)
//     {
//         first += i.first;
//         second += i.second;
//     }

//     std::pair<double, double> result = {first, second};

//     return result;
// }
