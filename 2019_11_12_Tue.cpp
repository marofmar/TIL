//
//  main.cpp
//  classCounter
//
//  Created by Yujin Chung on 12/11/2019.
//  Copyright © 2019 Yujin Chung. All rights reserved.
//

#ifndef COUNTER_H_INCLUDED

#define COUNTER_H_INCLUDED

class Counter { //declare a class named Counter
    int value;  // private data member
public:         // data member funtion
    void resset()
        { value = 0;}   // reset the value to 0
    void count()
        {++value;}      // add 1 to the value
    int getValue() const
        {return value;} // return the current value
    
};

#endif //COUNTER_H_INCLUDED
