#include "example.h"

void my_class::set_value(Complex a, const std::vector<Complex> v)
{
	com1 = {1,2};
	comV = v;
}

void my_class::print_value()
{
	std::cout << com1 << std::endl;
	for (int i=0; i<comV.size(); i++)
		std::cout<<comV[i]<<std::endl;

}

dim1C my_class::half(const std::vector<Complex>& v) 
{
    std::vector<Complex> w(v);
    for (int i=0; i<w.size(); i++)
        w[i] /= 2.0;
    return w;
}

dim2C my_class::half2(const dim1C& v)
{	
	dim2C w(v.size(), dim1C(2));
	for (int i=0; i<v.size(); i++){
		for (int j=0; j<2; j++)
			w[i][j] = v[i]/2.0;
	}
	return w;
}