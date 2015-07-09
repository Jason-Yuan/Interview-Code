//=============================================================================================================================
//      Project:                  Selection Sort
//      Time Complexity:          O(n2)
//      Space Complexity:         O(1)
//      Stability:                Not stable
//      Info:                     Decrease-by-one sorting
//=============================================================================================================================

#ifndef selectionSort
#define selectionSort

using namespace std;

// Selection Sort        
int* SelectionSort(int a[], int n)
{
	// declare a vector called unsorted_list and assign each element of input array into the vector
	vector<int> unsorted_list;
	unsorted_list.assign(a, a + n); 

	// create another vector, select the smallest element in unsorted_list each time, and append to it
	vector<int> sorted_list;
	while (!unsorted_list.empty())
	{
		int least = unsorted_list.front();
		int least_index = 0;
		for (int i = 0; i < unsorted_list.size(); ++i)
		{
			if (unsorted_list.at(i) < least)
			{
				least = unsorted_list.at(i);
				least_index = i;
			}
		}
		unsorted_list.erase(unsorted_list.begin() + least_index);
		sorted_list.push_back(least);
	}

	// convert vector(sorted_list) to array(result)
	int* result = &sorted_list[0];
	return result;
}

// In-place Selection Sort  
void Inplace_SelectionSort(int a[], int n)
{
	for (int i = 0; i < n; ++i)
	{
		int least_index = i;
		for (int j = i + 1; j < n; ++j)
		{
			if (a[j] < a[i])
			{
				least_index = j;
			}
		}

		// swap L[i] and L[least_index]
		int temp = a[i];
		a[i] = a[least_index];
		a[least_index] = temp;		
	}
}

#endif