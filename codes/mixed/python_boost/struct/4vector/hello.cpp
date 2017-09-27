#include <string>
#include <vector>

using std::string;
using std::vector;
using StateVec = std::vector<double>;
class Var
{
    public:
        double myFuncSet(const StateVec& A) 
        { 
            double tmp;
            for (int i=0; i<A.size(); i++)
                tmp += A[i];
            return  tmp/(double)A.size();
        }  
    // private:
    //     double average;  
};

#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>

using namespace boost::python;

BOOST_PYTHON_MODULE(hello)
{
    class_<StateVec>("StateVec")
        .def(vector_indexing_suite<StateVec>());
    
    class_<Var>("Var")
    .def("myFuncSet",&Var::myFuncSet)
    ;
}
