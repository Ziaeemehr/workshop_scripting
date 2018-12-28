#include <string>
struct World
{
    void set(std::string msg) { this-> msg = msg; }
    std::string greet() { return msg; }
    std::string msg;
};
 
#include <boost/python.hpp>
  
BOOST_PYTHON_MODULE(hello)
{
    using namespace boost::python;
    class_<World> ("World");
    def("greet", &World::greet);
    def("set", &World::set);
}
