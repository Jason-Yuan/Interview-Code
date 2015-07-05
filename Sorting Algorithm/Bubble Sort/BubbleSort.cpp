//=============================================================================================================================
//      Project:                  Bubble Sort
//      Time Complexity:          O(n2)
//      Space Complexity:         O(1)
//      Stability:                Stable
//=============================================================================================================================

#ifndef bubbleSort
#define bubbleSort

// Basic Bubble Sort
void BubbleSort(int a[], int n)
{
	int temp;
	for (int i = 0; i < n-1; ++i)
	{
		for (int j = 0; j < n-i-1; ++j)
		{
			if (a[j] > a[j+1])
			{
				temp = a[j];
				a[j] = a[j+1];
				a[j+1] = temp;
			}
		}
	}
}

// Bubble Sort with flag to indicate the index after which the array has been sorted
void BubbleSort2(int a[], int n)
{
	int temp;
	int flag = n-1;     // elements after flag should be sorted, at the begining, we assume all elements all unsorted.
	while (flag > 0)    // if flag = 0, the whole array has been sorted
	{
		int origin_flag = flag;       

		for (int i = 0; i < origin_flag; ++i)
		{
			if (a[i] > a[i+1])
			{
				flag = i;
				temp = a[i];
				a[i] = a[i+1];
				a[i+1] = temp;
			}
		}

		if ( flag == origin_flag)
		{
			flag = 0;
		}
	}
}

#endif