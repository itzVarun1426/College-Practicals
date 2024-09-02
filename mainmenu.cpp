#include<iostream>
#include<string>
using namespace std;
void add(int a , int b){
	cout<<"The addition is : "<<a+b;
	}
void sub(int a , int b){
	cout<<"The subtraction is : "<<a-b;
	}
void mult(int a , int b){
	cout<<"The multiplication is : "<<a*b;
	}
void div(int a , int b){
	cout<<"The division is : "<<a/b;
	}

int main(){
	int a , b , ch;
	string rep;
	do{
		cout<<"-------------------MENU-----------------------"<<endl;
		cout<<"1.ADDITION"<<endl;
		cout<<"2.SUBTRACTION"<<endl;
		cout<<"3.MULTIPLICATION"<<endl;
		cout<<"4.DIVISION"<<endl;
		cout<<"Enter the choice : "<<endl;
		cin>>ch;
		switch(ch){
			case 1:
				cout<<"You have chosen Addition ----"<<endl;
				cout<<"Enter the number : "<<endl;
				cin>>a;
				cout<<"Enter the number : "<<endl;
				cin>>b;
				add( a ,  b);
				break;
			case 2:
				cout<<"You have chosen Subtraction ------"<<endl;
				cout<<"Enter the number : "<<endl;
				cin>>a;
				cout<<"Enter the number : "<<endl;
				cin>>b;
				sub( a ,  b);
				break;
			case 3:
				cout<<"You have chosen Multiplication ------"<<endl;
				cout<<"Enter the number : "<<endl;
				cin>>a;
				cout<<"Enter the number : "<<endl;
				cin>>b;
				mult( a , b);
				break;
			case 4:
				cout<<"You have chosen Division ------"<<endl;
				cout<<"Enter the number : "<<endl;
				cin>>a;
				cout<<"Enter the number : "<<endl;
				cin>>b;
				div( a, b);
				break;
			default:
				cout<<"---INVALID INPUT---"<<endl;
				break;
		}
		cout<<"Do you want to try it again : (yes/no) "<<endl;
		cin>>rep;
	}
	while(rep=="yes");
	
	
				
return 0;
}
