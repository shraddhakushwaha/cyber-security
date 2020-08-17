#include<iostream>
#include<cstdlib>
using namespace std;
int main(int argc,char*argv[])
{
cout<<"number entered:"<<argc-1<<"\n";
int num[argc-1];
int i;
for(i=1;i<argc;i++)
num[i-1]=atoi(argv[i]);
int least=num[0];
for(i=1;i<argc-1;i++)
{
if(num[i]==least)
{
cout<<"hghghjg";
exit(0);
}
else if(num[i]<least)
least=num[i];
}
cout<<"least number is:"<<least<<endl;
return 0;}
