/*
Giving letter grade based on the input score value
*/

#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    // insert code here...
    int score;
    string grade;
    cout<<"Enter the score: ";
    cin >> score;
    switch(score/10){
        case 10:
        case 9: grade = 'A';
            break;
        case 8: grade = 'B';
            break;
        case 7: grade = 'C';
            break;
        case 6: grade = 'D';
            break;
        default: grade = 'F';
    }
    cout << "Letter grade: "<< grade <<endl;
    return 0;
}
