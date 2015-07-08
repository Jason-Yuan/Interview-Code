#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include "SelectionSort.cpp"

using namespace std;

int main()
{
	int a[10] = {2, 3, 5, 1, 7, 6, 8, 9, 10, 4};

	int* sorted_list = SelectionSort(a, 10);
	cout<<"SelectionSort: ";
	for (int i = 0; i < 10; ++i)
	{
		cout<<sorted_list[i]<<" ";
	}
	cout<<endl;

	Inplace_SelectionSort(a, 10);
	cout<<"Inplace SelectionSort: ";
	for (int i = 0; i < 10; ++i)
	{
		cout<<a[i]<<" ";
	}
	cout<<endl;

	return 0;
}