#include<iostream>
using namespace std;
int main()
{
int high,low,i,flag;
cout<<"enter the range of number:";
cout<<"first no.";
cin>>low;
cout<<"last no.";
cin>>high;
while(low<high)
{
flag=0;
for(i=2;i<=low/2;i++)
{
if(low%i==0)
{
flag=1;
break;
}}
if(flag==0)
cout<<low<<"";
low++;
}
return 0;
}
