/* File : example.h */

#include <vector>
#include <assert.h>

// std::vector<int> reorder_nodes(
//     const std::vector<int> &c,
//     const std::vector<int> &order,
//     const int N)
// {
//     assert(c.size()== N*N);
//     int n = c.size();
//     std::vector<int> reordered(n);
//     
//     for (int i = 0; i < N; i++)
//     {
//         for (int j = 0; j < N; j++)
//         {
//             reordered[N * i + j] = c[order[N * i + j]];
//         }
//     }
// 
//     return reordered;
// 
// }


int reorder_nodes(
    const std::vector<std::vector<int>> &c)
{
    int n = c.size();

    return n;

}
