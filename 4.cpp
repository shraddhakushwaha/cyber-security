#include<iostream>
#include<string.h>
using namespace std;
int main()
{
int i,x;
char a[100];
cout<<"choose following option:\n";
cout<<"1=encrypt the string \n";
cout<<"2=decrypt the string\n";
cin>>x;
cout<<"enter the string:";
cin>>a;
switch(x)
{
case 1:
for(i=0;(i<100 && a[i]!='\0');i++)
a[i]=a[i]+5;
cout<<"\n encrypt string:"<<a;
break;
case 2:
for(i=0;(i<100 && a[i]!='\0');i++)
a[i]=a[i]-5;
cout<<"\n decrypt string:"<<a;
break;
default:
cout<<"error";
}
return 0;
}
