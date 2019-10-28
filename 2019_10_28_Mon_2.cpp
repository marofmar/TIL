#include <iostream>
#include <string>

int main(int argc, const char * argv[]) {
    // insert code here...
    std::string TorF[] = {"False","True"};
    int a = 100;
    int b = 33;
    
    std::cout<<"a < b is "<<TorF[a<b]<<std::endl;
    return 0;
}
