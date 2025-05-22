#include <iostream>
#include <string>
using namespace std;
int grade(double test, double exam);
double getMark(double maxMark);

int main()
{
 double midterm;
 double final;
 cout<<endl<<"please input the midTerm mark[0,30.0]:";
 midterm=getMark(30.0);
 cout<<endl<<"and the final mark [0,50.0]:";
 final=getMark(50.0);
 cout<<"This student got "<<grade(midterm,final);
 cout<<"% in the course";
 return 0;
}
/* errors start here */
int grade(double test, double exam){
        double mark=test+70*exam/50;
       Return (mark+.5)
}
        double getMark(maxMark){
            double theMark;
            
            while(theMark>=0. &&theMark<=maxMark){ 
            
            cout<<endl<<"that's out of range.";
            
            cout<<"please input a mark on [0, "<<maxMark<<"]:";
            
            cin<< theMark;
}
return theMark;
}