/* SolutionCombiner.i */
%module SolutionCombiner
%{
    /* Put header files here or function declarations like below */
    #include "Coord.hpp"
    #include "MaterialData.hpp"
    #include "FailureCriterion.hpp"
    #include "QuadPointData.hpp"
    #include "ModelSolution.hpp"
    #include "ExclusionZone.hpp"
    #include "CriticalLocation.hpp"
    #include "FailureMode.hpp"
    #include "ExecutiveFunctions.hpp"

    #include <fstream>
    #include <iostream> 
%}
%{
    #define SWIG_FILE_WITH_INIT
    std::ostream& new_ofstream(const char* FileName){
        return *(new std::ofstream(FileName));
    }

    std::istream& new_ifstream(const char* FileName){
        return *(new std::ifstream(FileName));
    }

    void write(std::ostream* FOUT, char* OutString){
        *FOUT << OutString;
    }

    std::ostream *get_cout(){return &std::cout;}
%}

%include "std_vector.i"
%include "std_string.i"
%include "std_set.i"
%include "../../source/Coord.hpp"
%include "../../source/MaterialData.hpp"
%include "../../source/FailureCriterion.hpp"
%include "../../source/QuadPointData.hpp"
%include "../../source/ModelSolution.hpp"
%include "../../source/ExclusionZone.hpp"
%include "../../source/CriticalLocation.hpp"
%include "../../source/FailureMode.hpp"
%include "../../source/ExecutiveFunctions.hpp"

namespace std {
   %template(IntVector) vector<int>;
   %template(DoubleVector) vector<double>;
   %template(DoubleVVector) vector<vector<double> >;
   %template(DoubleVVVector) vector<vector<vector<double> > >;
   %template(SolutionVector) vector<ModelSolution>;
   %template(CritLocVector) vector<CriticalLocation>;
   %template(CritLocVVector) vector<vector<CriticalLocation> >;
   %template(ModeVector) vector<FailureMode>;
   %template(IntSet) set<int>;
}
std::ofstream& new_ofstream(char* FileName);
std::ifstream& new_ifstream(char* FileName);
std::iostream *get_cout();
