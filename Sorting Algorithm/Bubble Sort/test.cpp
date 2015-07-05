#include <iostream>
#include <string>
#include <cstring>
#include "BubbleSort.cpp"

using namespace std;

int main()
{
	int a[10] = {2, 3, 5, 1, 7, 6, 8, 9, 10, 4};

	BubbleSort(a, 10);
	cout<<"BubbleSort:"<<endl;
	for (int i = 0; i < 10; ++i)
	{
		cout<<a[i]<<endl;
	}

	BubbleSort2(a, 10);
	cout<<"BubbleSort2:"<<endl;
	for (int i = 0; i < 10; ++i)
	{
		cout<<a[i]<<endl;
	}
	
	return 0;
}