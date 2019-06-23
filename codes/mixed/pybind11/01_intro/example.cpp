#include <pybind11/pybind11.h>

namespace py = pybind11;

int add(int i, int j)
{
    return i + j;
}

int add_default(int i = 1, int j = 2)
{
    return i + j;
}

PYBIND11_MODULE(example, m)
{
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &add, "A function which adds two numbers.");

    // m.def("add", &add, "A function which adds two numbers.",
    //       py::arg("i"), py::arg("j"));

    m.def("add_default", &add_default,
          "A function which add two numbers with default arguments.",
          py::arg("i")=1, py::arg("j")=2);
    
    // regular notation for default arguments
    // m.def("add1", &add, py::arg("i") = 1, py::arg("j") = 2);
    // shorthand notation for default arguments
    // m.def("add2", &add, "i"_a=1, "j"_a=2);

    // exporting variables:
    m.attr("the_answer")=42;
    py::object word = py::cast("apple");
    m.attr("what") = word;


}