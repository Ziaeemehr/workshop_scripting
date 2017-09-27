#include <string>

using std::string;

struct Var
{
    Var (string name): name(name), value() {} //add constructor
    string const name;
    double value;
};


#include <boost/python.hpp>
using namespace boost::python;

BOOST_PYTHON_MODULE(hello)
{
    class_<Var>("Var",init<string>())
        .def_readonly("name", &Var::name)
        .def_readwrite("value", &Var::value)
    ;

}
