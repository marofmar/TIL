#include <iostream>
#include <string>

int main(int argc, const char * argv[]) {
    // insert code here...
    std::string TorF[] = {"False","True"};
    int a = 100;
    int b = 33;
    int A = 3;
    int B = 6;
    int C = 9;
    int D = 12;
    
    std::cout<<"a < b is "<<TorF[a<b]<<std::endl;
    
    std::cout<<"(A ==C) && (B > D) is "<<TorF[(A ==C) && (B > D)];

    //A true || false = true
    std::cout<<"\n(A ==C) || (B == D) is "<<TorF[(A ==C) || (B == D)]<<std::endl;
    return 0;
}
