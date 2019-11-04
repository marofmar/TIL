/"
-Learn about 'struct'
-By far the longest code of mine in C++
"/


//
//  main.cpp
//  circleCircle
//
//  Created by Yujin Chung on 01/11/2019.
//  Copyright © 2019 Yujin Chung. All rights reserved.
//

#include <iostream>
#include <cmath>

using namespace std;

const double PI = 3.141593;

struct C2dType { //2-dim cooridnates structure
    double x, y;
};

struct CircleType{ //Circle structure
    C2dType center; //center coordinates
    double radius; //radius of a circle
};

double circleArea(CircleType c)
{
    return c.radius*c.radius*PI;
}

bool chkOverlap(CircleType c1, CircleType c2)
{
    double dx = c1.center.x - c2.center.x;
    double dy = c1.center.y - c2.center.y;
    double dCntr = sqrt(dx*dx + dy*dy);
    return dCntr < c1.radius + c2.radius;
}

void dispCircle(CircleType c)
{
    cout <<"Center: ("<<c.center.x<<","<<c.center.y<<")";
    cout <<"Radius: "<<c.radius<<endl;
}


int main()
{
    CircleType c1 = {{0,0},10}; // center (0,0), radius 10 initialize
    CircleType c2 = {{30,10}, 5}; // center(30,10) radius 5 initialize
    
    cout <<"Circle 1 " << endl;
    dispCircle(c1);
    cout<<"Circle 1's Area: "<<circleArea(c1)<<endl;
    cout<<"Circle 2 " << endl;
    dispCircle(c2);
    cout<<"Circle 2's Area: " << circleArea(c2)<<endl;
    
    // Print out whether they overlap or not
    if (chkOverlap(c1, c2))
        cout << "They overlap each other."<<endl;
    else
        cout << "They do not overlap." <<endl;
    
    
    return 0;
}
