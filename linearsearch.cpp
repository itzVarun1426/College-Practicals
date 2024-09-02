#include<iostream>
#include<string>
using namespace std;
int main(){
int arr[10];
int index,ele;

for(int i=0 ; i<10 ; i++)
{
cout<<"Enter the " <<i+1 <<" th element : "<<endl;
cin>>arr[i];
}
cout<<"The elements in array are : "<<endl;
for(int i=0; i<10 ;i++)
{
cout<<arr[i] <<" ";
}
cout<<endl<<"Enter the element to search in array :"<<endl;
cin>>ele;
for(int i=0 ; i<10 ; i++)
{
if(arr[i]==ele){
index=i;
}
}
cout<<ele <<" this element is at " << index <<" index position"<<endl;
return 0;
}
