//=============================================================================================================================
//      Project:                  Merge Sort
//      Time Complexity:          O(nlogn)
//      Space Complexity:         O(1)
//      Stability:                Stable
//      Info:                     Decrease by half pattern (Divide and Conquer)
//=============================================================================================================================

#ifndef mergeSort
#define mergeSort

// merge array A and B into S
void Merge(int *S, int *A, int aSize, int *B, int bSize)
{
	int ai = 0;	// index of array A
	int bi = 0;	// index of array B
	int si = 0;	// index of array S
	while (ai < aSize && bi < bSize)
	{
		if (A[ai] <= B[bi]) S[si++] = A[ai++];
		else S[si++] = B[bi++];
	}
	while (ai < aSize) 
	{
		S[si++] = A[ai++];
	}
	while (bi < bSize) 
	{
		S[si++] = B[bi++];
	}
}

void MergeSort(int a[], int n)
{
	int half, *A, *B;
	// base condition
	if (n <= 1)
	{
		return;
	}

	// divide to A and B
	half = n / 2;
	A = new int[half];
	B = new int[n-half];

	for (int i = 0; i < half; ++i)
	{
		A[i] = a[i];
	}
	for (int i = half; i < n; ++i)
	{
		B[i-half] = a[i];
	}

	MergeSort(A, half);
	MergeSort(B, n-half);
	Merge(a, A, half, B, n-half);

	// detetion
	delete [] A;
	delete [] B;
}

#endif