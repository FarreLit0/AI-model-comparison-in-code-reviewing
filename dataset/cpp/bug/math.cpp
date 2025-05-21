#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int square(int a){
    return a*a;
}
struct  Point{
    int x,y;

};
int distance (const  Point& a,const Point& b){
    int k=(int) sqrt((float)((a.x-b.x)*(a.x-b.x))+((a.y-b.y)*(a.y-b.y)));
    return k;

}
int main(){

    vector<Point>a(10);
    for (int i=0;i<10;i++){
        cin>>a[i].x>>a[i].y;
    }

    int s=0;
    int s1;
    int k=0; 
    for (int i=1;i<10;i++){

        s+=square(distance(a[0],a[i]));
    }
    for (int i=1;i<10;i++){
        s1=0;
        for (int j=0;j<10;j++){
            s1+=square(distance(a[i],a[j]));

            if (s1<s) {  s=s1; k=i;}

        }
    }
    cout<<k<<"Points are:";
    cout<<a[k].x;
    cout<<a[k].y;


    return 0;
}