/*
How to make declare const, var
using cout and cin
const PI can be repalce later if I use cmath perhaps
*/

#include <iostream>

using namespace std;

int main() {
    const double PI {3.14159};
    double radius;
    
    cout << "Enter the radius value: ";
    cin >> radius;
    
    double area = radius * radius * PI;
    cout << "Area of the circle = " << area << endl;
    return 0;
}
