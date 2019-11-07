/*
- Pointer study
- While {condition} {
    code block to execute
   }
- very interesting the computation, *pt = *pt -"a" +"A" 
*/


//
//  main.cpp
//  arrayPtr
//
//  Created by Yujin Chung on 07/11/2019.
//  Copyright © 2019 Yujin Chung. All rights reserved.
//

#include <iostream>
using namespace std;


int main() {
    // insert code here...
    //std::cout << "Hello, World!\n";
    
    char str[14] = "Hello, world!"; //13 characters + null = 14
    char *pt;
    
    cout << str << endl;
    pt = str; //pt points to str
    while (*pt){
        if(*pt >='a' && *pt<='z')
            *pt = *pt - 'a' +'A';
        pt++;
    
}

    cout<<str<<endl;
    
    
    
    return 0;
}
