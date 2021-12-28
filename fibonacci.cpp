#include<iostream>
#include<math.h>
#include<iomanip>
#include<stdio.h>
#include<conio.h>
using namespace std;

int fib(int n)
{
    int a = 0, b = 1, c, i;
    if( n == 0)
        return a;
    for(i = 2; i <= n; i++)
    {
       c = a + b;
       a = b;
       b = c;
    }
    return b;
}

float f(double x)
{
    return pow(x,3)*(x-3)*pow((x-6),4);  //enter function here
    
}
//in this question (4,7) is the uncertainity region and n=3
int main()
{
    double a,b;
    int n;
    int k=2;
    int L;
    double x1,x2,Lk;
    cout<<"Enter the limits\n";
    cin>>a>>b;
    fflush(stdin);
    cout<<"Enter the Number of Function Evaluvations\n";
    cin>>n;
    cout<<endl;
    L = (b-a);
    cout<<"The value of L is :"<<L<<endl;
    while(k<=n)
    { 
        cout<<"\n \n";
        cout<<"The "<<(k-1)<<"th Iteration :"<<endl;
        int I_0 = (n-k+1);
        int I_1 = (n+1);
        int F_0 = fib(I_0+1);
        int F_1 = fib(I_1+1);
        Lk = ((double)F_0/(double)F_1)*L;
        cout<<" The Value of I_0 :"<<I_0<<endl;
        cout<<" The Value of I_1 :"<<I_1<<endl;
        cout<<" The Value of F_0 :"<<F_0<<endl;
        cout<<" The Value of F_1 :"<<F_1<<endl;
        cout<<" The Value of L_"<<k<<"  is :"<<Lk<<endl;
        x1 = a + Lk;
        x2 = b - Lk;
        cout<<"x1 :"<<x1<<endl;
        cout<<"x2 :"<<x2<<endl;
        cout<<" f(x1) : "<<f(x1)<<"\n f(x2) : "<<f(x2)<<endl;
        if(f(x1) == f(x2))
        {
            a = x1;
            b = x2;
        }
        else if(f(x1)>f(x2))
        {
            a = x1;
        }
        else
        {
            b = x2;
        }
        k++;
        cout<<"\n The Values of a : "<<a<<"\n The Values of b :"<<b<<endl;
    }

    cout<<"\n The Interval in which minimum lies ["<<a<<","<<b<<"] .";
}
