#include <sstream>
#include <vector>
#include <cmath>
#include <numeric>
#include <iostream>
using namespace std;

int main (int argc, char** argv)
{
    b2Vec2 gravity(0.0f, -10.0f);
    b2World world(gravity);
    cout << "hello world" << endl; 
    return 0; 
}

class Atom 
{
    public:
        Atom();
};