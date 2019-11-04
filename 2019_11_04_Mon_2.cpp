/*
Finding the Max value out of an array! 
*/


//
//  main.cpp
//  letsFindMax
//
//  Created by Yujin Chung on 04/11/2019.
//  Copyright © 2019 Yujin Chung. All rights reserved.
//

#include <iostream>

using namespace std;

int main()
{
    int max;
    int data[10] = {10,23,5,9,2,47,64,238,120,1};
    
    max = data[0]; // let's set the first one as the maximum (initialize)
    cout << "Data: "<<data[0]; // print out the first
    
    for (int i = 1; i < 10; i++) {
        cout << " " << data[i]; // print out the i-th data
        if (max < data[i]) max = data[i]; // if the i-th is bigger than max, then i-th is the new MAX
    }
    cout << " \n\nThe Maximum of the data: " << max << endl;
    
    return 0;
    
}

