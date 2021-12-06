#include <iostream>
#include <string>
#include "Simbody.h"
using namespace SimTK;

using std::string;
using std::endl;
using std::cout;

using namespace std;
int main()
{
    string mystring = " print this ";
    cout << "Hello, World!" << " This is cool "  << mystring << 3.14158334 << endl;

    int* p = new int;
    *p = 5;
    cout << p <<  " value " << *p << endl;
    p = new int(3); 
    cout << p << " value " << *p << endl;
    



    return 0;
}
