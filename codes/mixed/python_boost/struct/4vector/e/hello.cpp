#include <string>
#include <vector>

using std::string;
using std::vector;
using StateVec = std::vector<double>;
struct Var
{
    StateVec arr;
    void set(int N) 
    { 
        StateVec A;
        for (int i=0; i<N; i++)
            A[i] = 2.0 * i;
        arr = A;
    }    
};

#include <boost/python.hpp>
using namespace boost::python;

BOOST_PYTHON_MODULE(hello)
{
    class_<Var>("Var")
        .def("init", &Var::set)
    ;
}
