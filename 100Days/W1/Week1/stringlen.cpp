#include <iostream>
#include <string.h>
using namespace std;
int main()
{
    string name;
    cout<<"Hello \nWhat is your name? ";
    cin>>name;
    cout<<"Welcome to C++ "+name+ "!\n";
    char response;
    cout<<"See the length of your name ? (y/n) ";
    cin>>response;
    if (response == 'y')
        cout<<"The length of your name is "+to_string(name.length());
    else
        cout<<"Goodbye";
    return 0;
}