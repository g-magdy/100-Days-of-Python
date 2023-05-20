#include <iostream>
using namespace std;
int main()
{
    srand(time(0));
    cout << "Hello, Let's flip some coins\n";
    int target_n;
    do
    {
        cout << "enter the number of heads you'd like to reach in a row: ";
        cin >> target_n;
        if (target_n < 1)
            cout << "negatives are not allowed!\n";
    } while (target_n < 1);
    int flips_counter = 0;
    int streak = 0;
    int flip;
    while (streak < target_n)
    {
        flip = rand() % 2;
        flips_counter++;
        if (flip)
            streak++;
        else
            streak = 0;
    }
    printf("Congratulations, we have flipped %i heads in a row after %i total flips", target_n, flips_counter);
    return 0;
}