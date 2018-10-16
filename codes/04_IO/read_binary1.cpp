#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <iostream>
 
using namespace std;

int main( void ) {
  std::ifstream in( "a.bin", std::ios::binary );
  vector<double> vs;
  if ( in ) {
    std::vector<double> vs;
    vs.insert( vs.begin(), std::istream_iterator<double>(in), std::istream_iterator<double>() );
    std::copy( vs.begin(), vs.end(), std::ostream_iterator<int>(std::cout, "\n"));
  }

  cout << vs.size() <<"\n"; 
 
  return 0;
}