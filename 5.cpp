#include<iostream>
#include<string.h>
using namespace std;
int main()
{
char a[10],i,n,j,k,l,m;
cout<<"string=";
cin>>a;
n=strlen(a);
for(i=0;i<n;i++)
{
 if((i+1)%2!=0)
{
if(97<=a[i]||a[i]<=122)
{

for(j=0;j<=(a[i]-97);j++)
{
cout<<"#";
}
}
else
{
for(k=0;k<=(a[i]-65);k++)
{
cout<<"#";
}
}
}
else
{
if(97<=a[i]||a[i]<=122)
{
for(l=0;l<=(a[i]-97);l++)
{
cout<<"$";
}
}
else
{
for(m=0;m<=(a[i]-65);m++)
{
cout<<"$";
}
}
}
}}
