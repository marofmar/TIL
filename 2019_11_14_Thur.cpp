//
//  main.cpp
//  funcOverloading
//
//  Created by Yujin Chung on 14/11/2019.
//  Copyright © 2019 Yujin Chung. All rights reserved.
//

#include <iostream>
using namespace std;

struct TimeRec{
    int hours;
    int minutes;
};

// Adding time func
// var TimeRec &t1 : now time
//              const TimeRec &t2 : time that will be added
// return value None

void AddTime(TimeRec &t1, const TimeRec &t2)
{
    t1.minutes += t2.minutes;
    t1.hours += t2.hours + t1.minutes/60;
    t1.minutes %= 60;
}

// Adding time func
// var TimeRec &t : now time (current time)
//      int minutes : minute-time that will be added to the current one
// return value None
void AddTime(TimeRec &t, int minutes)
{
    t.minutes += minutes;
    t.hours += t.minutes/60;
    t.minutes %=60;
    
}

int main()
{
    TimeRec tRec1 = {2, 30};
    TimeRec tRec2 = {1, 45};
    
    cout << tRec1.hours <<" hour "<<tRec1.minutes<<" minutes + ";
    cout << tRec2.hours <<" hour "<<tRec2.minutes<<" minutes = ";
    AddTime(tRec1, tRec2);
    cout << tRec1.hours << " hours "<<tRec1.minutes<<" minutes"<<endl;
    
    cout<<tRec1.hours<<" hours "<<tRec1.minutes <<" minutes + ";
    cout << "135 minutes = ";
    AddTime(tRec1, 135);
    cout << tRec1.hours<< " hours "<< tRec1.minutes << " minutes"<<endl;
    
    return 0;
}
