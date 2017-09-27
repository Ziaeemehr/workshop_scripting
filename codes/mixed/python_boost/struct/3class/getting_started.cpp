#include <iostream>
#include <string>

using std::string;

namespace {  // Avoid cluttering the global namespace.
    // A friendly class.
    class hello
    {
        public:
            hello(const string& country) 
            { 
                this->country = country;
            }
            string greet() const 
            {
                return "Hello from " + country;
            }
        private:
            string country;
    };
    // A function taking a hello object as an argument.
    string invite(const hello& w)
    {
        return w.greet() + "!please come soon!";
    }
}



#include <boost/python.hpp>
using namespace boost::python;

BOOST_PYTHON_MODULE(getting_started)
{
    class_<hello>("hello",init<string>())
        .def("greet", &hello::greet) // Add a regular member function.
        .def("invite", invite)       // Add invite() as a regular function to the module.
    ;
    def("invite", invite);           // Even better, invite() can also be made a member of module!!!
}
