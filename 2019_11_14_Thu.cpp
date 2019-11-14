//
//  main.cpp
//  cStyleStr
//
//  Created by Yujin Chung on 14/11/2019.
//  Copyright © 2019 Yujin Chung. All rights reserved.
//

#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    char str1[40] = "C style string"; //
    char str2[] = "Object-Oriented "; // size of the array = length of the string
    const char *str3 = "Programming"; // char pointer
    
    cout << str1 << endl; // print the string
    cout << str3 << "'s string length is ";
    cout <<strlen(str3) << endl; // strlen() : length of the string
    strcpy(str1, str2); // strpy() copying the string
    cout << str1 << endl;
    strcat(str1, str3); // concatenate strings
    cout << str1 << endl;
    return 0;

}
