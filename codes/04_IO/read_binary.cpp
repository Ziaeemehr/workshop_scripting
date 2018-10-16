// reading an entire binary file
#include <iostream>
#include <fstream>
#include <iostream>
#include <iterator>
#include <vector>

using namespace std;


std::vector<double> readFile(const char* filename)
{
    // open the file:
    std::ifstream file(filename, std::ios::binary);

    // Stop eating new lines in binary mode!!!
    file.unsetf(std::ios::skipws);

    // get its size:
    std::streampos fileSize;

    file.seekg(0, std::ios::end);
    fileSize = file.tellg();
    file.seekg(0, std::ios::beg);

    // reserve capacity
    std::vector<double> vec;
    vec.reserve(fileSize);

    // read the data:
    vec.insert(vec.begin(),
               std::istream_iterator<double>(file),
               std::istream_iterator<double>());

    return vec;
}



int main () {
  // streampos size;
  // char * memblock;

  // ifstream file ("a.bin", ios::in|ios::binary|ios::ate);
  // if (file.is_open())
  // {
  //   size = file.tellg();
  //   memblock = new char [size];
  //   file.seekg (0, ios::beg);
  //   file.read (memblock, size);
  //   file.close();

  //   cout << "the entire file content is in memory \n";

  //   delete[] memblock;
  // }
  // else cout << "Unable to open file";

  auto vec = readFile("a.bin");
  for (auto v : vec)
    cout << v << endl;


  return 0;
}




// #include <iostream>
// #include <fstream>
// #include <vector>
// using namespace std;

// int main () 
// {
//   vector<double> V;
//   ifstream in("a.bin", ios::in | ios::binary);
//   in.read((char *) &V[0], sizeof(double)); 

//   // see how many doubles have been read
//   cout << in.gcount() << " doubles read\n"; 
//   // for(i=0; i<4; i++) // show values read from file
//   // cout << fnum[i] << " ";
//   // cout << "\n";
//   in.close();

// }