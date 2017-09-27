#include <string>

// using std::string;

struct World
{
    World (std::string msg): msg(msg) {} //add constructor
    World (double a, double b) {}        //add another constructor 
    void set(std::string msg) { this->msg = msg; }
    std::string greet() { return msg; }
    std::string msg;
};

#include <boost/python.hpp>
using namespace boost::python;

BOOST_PYTHON_MODULE(hello)
{
    // class_<World>("World")
    class_<World>("World",init<std::string>())
        .def(init<double,double>())
        .def("greet", &World::greet)
        .def("set", &World::set)
    ;
}
