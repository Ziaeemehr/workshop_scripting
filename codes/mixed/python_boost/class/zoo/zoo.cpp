/*
 * This inclusion should be put at the beginning.  It will include <Python.h>.
 */
#include <boost/python.hpp>
#include <cstdint>
#include <string>
#include <vector>
#include <boost/utility.hpp>
#include <boost/shared_ptr.hpp>

/*
 * This is the C++ function we write and want to expose to Python.
 */
const std::string hello() {
    return std::string("hello, zoo");
}

/*
 * Create a C++ class to represent animals in the zoo.
 */
class Animal {
public:
    // Constructor.  Note no default constructor is defined.
    Animal(std::string const & in_name): m_name(in_name) {}
    // Copy constructor.
    Animal(Animal const & in_other): m_name(in_other.m_name) {}
    // Copy assignment.
    Animal & operator=(Animal const & in_other) {
        this->m_name = in_other.m_name;
        return *this;
    }

    // Utility method to get the address of the instance.
    uintptr_t get_address() const {
        return reinterpret_cast<uintptr_t>(this);
    }

    // Getter of the name property.
    std::string get_name() const {
        return this->m_name;
    }
    // Setter of the name property.
    void set_name(std::string const & in_name) {
        this->m_name = in_name;
    }

private:
    // The only property: the name of the animal.
    std::string m_name;
};

/*
 * This is a macro Boost.Python provides to signify a Python extension module.
 */
BOOST_PYTHON_MODULE(zoo) {
    // An established convention for using boost.python.
    using namespace boost::python;

    // Expose the function hello().
    def("hello", hello);

    // Expose the class Animal.
    class_<Animal>("Animal",
        init<std::string const &>())
        .def("get_address", &Animal::get_address)
        .add_property("name", &Animal::get_name, &Animal::set_name)
    ;
}