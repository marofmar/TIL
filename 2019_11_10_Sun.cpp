/*
Converting Fahrenheit to Celcius
C++ Function study starter!
*/

//
//  main.cpp
//  convertFtoC
//
//  Created by Yujin Chung on 10/11/2019.
//  Copyright © 2019 Yujin Chung. All rights reserved.
//

#include <iostream>
using namespace std;

// a function converting fahrenheit to Celcius
// float fahr, for fahrenheit value

float FahrToC(float fahr) {
    return (fahr-32)*5/9;
}

int main()
{
    float fTemp, cTemp;
    cout << "Fahrenheit: ";
    cin >> fTemp;
    cTemp = FahrToC(fTemp); // calling the function
    cout << "------>Celcius: "<<cTemp<<endl;
    return 0;
}
