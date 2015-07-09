#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include "QuickSort.cpp"

using namespace std;

int main()
{
	int a[10] = {2, 3, 5, 1, 7, 6, 8, 9, 10, 4};
	vector<int> vector_a;
	vector_a.assign(a, a + 10) ; 
	vector<int> sorted_a = Deterministic_QuickSort(vector_a);
	cout<<"Deterministic_QuickSort: ";
	for (int i = 0; i < sorted_a.size(); ++i)
    {
    	cout<<sorted_a.at(i)<<' ';
    }
	cout<<endl;

	int b[10] = {2, 3, 5, 1, 7, 6, 8, 9, 10, 4};
	vector<int> vector_b;
	vector_b.assign(b, b + 10) ; 
	vector<int> sorted_b = Randomized_QuickSort(vector_b);
	cout<<"Randomized_QuickSort: ";
	for (int i = 0; i < sorted_b.size(); ++i)
    {
    	cout<<sorted_b.at(i)<<' ';
    }
	cout<<endl;

	int c[10] = {2, 3, 5, 1, 7, 6, 8, 9, 10, 4};
	Inplace_QuickSort(c, 0, 10);
	cout<<"Inplace_QuickSort: ";
	for (int i = 0; i < 10; ++i)
    {
    	cout<<c[i]<<' ';
    }
	cout<<endl;
	
	return 0;
}