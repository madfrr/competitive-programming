#include <bits/stdc++.h>
using namespace std;

int main()
{
    // Inputs and outputs
    cout << "banana\n";
    int a, b;
    string x;

    cin >> a >> b >> x;
    cout << a << " " << b << " " << x << "\n";
    /*
    NOTE 1:
    Sometimes, when input and output bottlenecks the programm, the snippet below is really useful
    ios::sync_with_stdio(0);
    cin.tie(0);
    */
    /*
    NOTE 2:
    \n is faster than endl. endl always causes a flush operation.
    */

    // To read a line
    string s;
    getline(cin, s);
    cout << s;

    //read infinity
    int count = 0;
    while (cin >> x) {
        cout << x;
        count ++;
        if (count == 10) {
            break;
        }
    }

    //
}