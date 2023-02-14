#include <iostream>
#include <cstdio>
using namespace std;

/*
Some C++ data types, their format specifiers, and their most common bit widths are as follows:

Int ("%d"): 32 Bit integer
Long ("%ld"): 64 bit integer
Char ("%c"): Character type
Float ("%f"): 32 bit real value
Double ("%lf"): 64 bit real value
*/

int main()
{
    int a;
    long b;
    char c;
    float d;
    double e;

    cin >> a >> b >> c >> d >> e;

    printf("%d\n%ld\n%c\n%.3f\n%.9lf", a, b, c, d, e);

    return 0;
}