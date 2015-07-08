#include <iostream>
#include <string>
#include <cstring>
#include "InsertionSort.cpp"

using namespace std;

int main()
{
	int a[10] = {2, 3, 5, 1, 7, 6, 8, 9, 10, 4};

	Inplace_InsertionSort(a, 10);
	cout<<"Inplace_InsertionSort: ";
	for (int i = 0; i < 10; ++i)
	{
		cout<<a[i]<<" ";
	}
	cout<<endl;

	return 0;
}