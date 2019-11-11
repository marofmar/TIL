/*
Inline Function in C++
*/

//
//  main.cpp
//  swapInline
//
//  Created by Yujin Chung on 11/11/2019.
//  Copyright © 2019 Yujin Chung. All rights reserved.
//

#include <iostream>
using namespace std;

//changing the values of two different variables
//return void

inline void SwapValues(int &x, int &y)
{
    int temp = x;
    x = y;
    y = temp;
}

int main()
{
    int a, b;
    cout << "Enter two integers: ";
    cin >> a >> b;
    if (a<b) SwapValues(a,b);
    cout << "Bigger = " << a<<", smaller = "<< b<< endl;
    return 0;
}

