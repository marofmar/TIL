/*
- Declare pointer by adding "*" in front.
- After declaring the pointer, we have to make the pointer variable to point a memory.
- &a means a's address
- To access the memory where the pointer directs, we use indirection operator "*"
*/




//
//  main.cpp
//  LetsStudyPointers
//
//  Created by Yujin Chung on 05/11/2019.
//  Copyright © 2019 Yujin Chung. All rights reserved.
//

#include <iostream>
using namespace std;


int main() {
    int a = 10;
    int *ptr;
    
    ptr =&a; // a's address has been saved to ptr variable
    
    cout << "The value prt is pointing at: "<<*ptr<<endl;
    *ptr = 20;
    cout << "The value of a: " << a<< endl;
    return 0;
}
