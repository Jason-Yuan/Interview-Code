//=============================================================================================================================
//      Project:                  Quick Sort
//      Time Complexity:          Expected O(nlogn) / Worst case O(n2)  
//      Space Complexity:         O(1)
//      Stability:                Not stable
//      Info:                     1. Decrease-by-half sorting, so bears some resemblance to merge sort.
//                                2. In quick sort algorithm, a pivot is an element of L used to divide L into three sub_lists.
//                                3. We hope the division process can divide L into two sub-lists of "roughly equal size".
//=============================================================================================================================

#ifndef quickSort
#define quickSort

using namespace std;

// First method, deterministic quick sort 
// worst-case time complextity is O(n2)
vector<int> Deterministic_QuickSort(vector<int> a)
{
	if (a.size() <= 1)
	{
		return a;
	}
	else
	{
		int pivot = a[0];
		vector<int> LT;	// LT means "less than pivot"
		vector<int> EQ;	// EQ means "equal to pivot"
		vector<int> GT;	// GT means "greater than pivot"
		for (int i = 0; i < a.size(); ++i)
		{
			if (a[i] < pivot)
			{
				LT.push_back(a[i]);
			}
			else
			{
				if (a[i] == pivot)
				{
					EQ.push_back(a[i]);
				}
				else
				{
					GT.push_back(a[i]);
				}
			}
		}
		vector<int> LT_S = Deterministic_QuickSort(LT);
		vector<int> GT_S = Deterministic_QuickSort(GT);

		LT_S.insert(LT_S.end(), EQ.begin(), EQ.end());
		LT_S.insert(LT_S.end(), GT_S.begin(), GT_S.end());

		return LT_S;
	}
}


// Second method, randomized quick sort, we need to use the random library
// Try to make O(n2)-time scenario less likely to occur.

vector<int> Randomized_QuickSort(vector<int> a)
{
	if (a.size() <= 1)
	{
		return a;
	}
	else
	{
		srand (time(NULL));
		int random_index = rand() % a.size();
		int pivot = a[random_index];

		vector<int> LT;	// LT means "less than pivot"
		vector<int> EQ;	// EQ means "equal to pivot"
		vector<int> GT;	// GT means "greater than pivot"
		for (int i = 0; i < a.size(); ++i)
		{
			if (a[i] < pivot)
			{
				LT.push_back(a[i]);
			}
			else
			{
				if (a[i] == pivot)
				{
					EQ.push_back(a[i]);
				}
				else
				{
					GT.push_back(a[i]);
				}
			}
		}
		vector<int> LT_S = Deterministic_QuickSort(LT);
		vector<int> GT_S = Deterministic_QuickSort(GT);

		LT_S.insert(LT_S.end(), EQ.begin(), EQ.end());
		LT_S.insert(LT_S.end(), GT_S.begin(), GT_S.end());

		return LT_S;
	}
}

// Third method, in-place quick sort
// Try to avoid the cost of allocating fresh data structures to store its output.

void Swap(int & a, int & b)
{
    int temp = a;
    a = b;
    b = temp;
}

pair<int, int> Inplace_Partition(int a[], int s, int e)
{
	srand (time(NULL));
	int random_index = rand() % (e - s) + s;
	int pivot = a[random_index];

	// first pass: partition L into LT, GE zones
	int lt_end = s;
	int ge_start = e;
	while (lt_end < ge_start)
	{
		if (a[lt_end] < pivot)
		{
			lt_end++;
		}
		else
		{
			if (a[ge_start - 1] >= pivot)
			{
				ge_start--;
			}
			else
			{
				Swap(a[lt_end], a[ge_start - 1]);
				lt_end++;
			}
		}
	}

	// second pass: partition GE into EQ, GT zones
	int eq_end = lt_end;
	int gt_start = e;
	while (eq_end < gt_start)
	{
		if (a[eq_end] == pivot)
		{
			eq_end++;
		}
		else
		{
			if (a[gt_start - 1] > pivot)
			{
				gt_start--;
			}
			else
			{
				Swap(a[eq_end], a[gt_start - 1]);
				eq_end++;
			}
		}
	}
	pair<int, int> result;
	result.first = lt_end;
	result.second = gt_start;
	return result;
}

void Inplace_QuickSort(int a[], int s, int e)
{
	if ((e - s) > 1)
	{
		int lt_end, gt_start;
		pair<int, int> result = Inplace_Partition(a, s, e);
		lt_end = result.first;
		gt_start = result.second;
		Inplace_QuickSort(a, s, lt_end);
		Inplace_QuickSort(a, gt_start, e);
	}
}

#endif