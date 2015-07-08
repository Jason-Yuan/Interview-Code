#include <iostream>
#include <string>
#include <cstring>
#include "MergeSort.cpp"

using namespace std;

int main()
{
	int a[10] = {2, 3, 5, 1, 7, 6, 8, 9, 10, 4};
	MergeSort(a, 10);
	cout<<"MergeSort: ";
	for (int i = 0; i < 10; ++i)
	{
		cout<<a[i]<<" ";
	}
	cout<<endl;

	return 0;
}