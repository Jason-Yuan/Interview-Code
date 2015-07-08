//=============================================================================================================================
//      Project:                  Insertion Sort
//      Time Complexity:          O(n2)
//      Space Complexity:         O(1)
//      Stability:                Stable
//      Info:                     Decrease-by-one sorting
//=============================================================================================================================

#ifndef insertionSort
#define insertionSort

// In-place insertion sorting
void Inplace_InsertionSort(int a[], int n)
{
	for (int i = 0; i < n; ++i)
	{
		int currentvalue = a[i];

		while (i > 0 && a[i-1] > currentvalue)
		{
			a[i] = a[i-1];
			i--;
		}

		a[i] = currentvalue;
	}
}

#endif