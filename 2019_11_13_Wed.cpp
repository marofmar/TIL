// Note: Using "const" to prevent the value being changed, while using reference calling on a function
//  main.cpp
//  constReferenceFunc
//
//  Created by Yujin Chung on 13/11/2019.
//  Copyright © 2019 Yujin Chung. All rights reserved.
//

#include <iostream>
using namespace std;

struct SalesRec {
    char pID[10];
    int dYear, dMonth, dDate;
    char deliverAddrs[40];
};

void PrSalesRec(const SalesRec &srec);

int main() {
    SalesRec s = {"ABC123", 2019, 11, 13, "Shadyside, Pittsburgh"};
    PrSalesRec(s);
    return 0;
}

void PrSalesRec(const SalesRec &srec)
{
    cout <<"Product Code: "<<srec.pID<<endl;
    cout <<"Delivery Date: " <<srec.dYear<<"-";
    cout <<srec.dMonth<<"-";
    cout<<srec.dDate<<endl;
    cout<<"Delivery Address: "<<srec.deliverAddrs<<endl;
}
