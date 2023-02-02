#include <iostream>
using namespace std;
int main()
{
    srand(time(0));
    int r = rand() % 11;
    cout<<r;
    return 0;
}