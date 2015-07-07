#include <iostream>
#include <cstring>
#include <cstdlib>
#include <string>

using namespace std;

//=============================================================================================================================
//      Project:                  Chapter 1-1 Method 1
//      Ideas:                    Assume we have 256 ASCII characters, we set up a array of 256 flags. Iterate each char in 
//                                the given string, first convert it to value of the byte(e.g. 97), then check if the flag 
//                                of array[97] is true, turn it to false, if the flag of array[97] is false, return false.
//      Time Complexity:          O(n)
//      Space Complexity:         O(1)
//=============================================================================================================================

bool isAllUniqueChar(string s)
{
	bool Flag[256];
	for (int i = 0; i < 256; ++i)
	{
		Flag[i] = true;
	}
	for (int i = 0; i < s.length(); i++)
	{
		if (Flag[s[i]])
		{
			Flag[s[i]] = false;
		}
		else
		{
			return false;
		}
	}
	return true;
}

//=============================================================================================================================
//      Project:                  Chapter 1-1 Method 2
//      Ideas:                    First, sort the stirng, if there are duplicates in the given string, they should be 
//                                neighbor then. Iterate each element in the stirng to see if the neighbors are same.
//      Time Complexity:          O(nlogn)
//      Space Complexity:         O(1)
//=============================================================================================================================

// Start pre-defined quicksort
// input: a string
// output: a string sorted in alphabeta order

string Randomized_QuickSort(string s)
{
	if (s.length() <= 1)
	{
		return s;
	}
	else
	{
		// # if a stirng is longer than 256 or is None, return false
		srand (time(NULL));
		int random_index = rand() % s.length();
		char pivot = s[random_index];
		string LT, EQ, GT, Sorted_LT, Sorted_GT;
		LT = EQ = GT = Sorted_LT = Sorted_GT = "";
		for (int i = 0; i < s.length(); ++i)
		{
			if (s[i] < pivot)
			{
				LT += s[i];
			}
			else
			{
				if (s[i] == pivot)
				{
					EQ += s[i];
				}
				else
				{
					GT += s[i];
				}
			}
		}
		Sorted_LT = Randomized_QuickSort(LT);
		Sorted_GT = Randomized_QuickSort(GT);

		return Sorted_LT + EQ + Sorted_GT;
	}
}
// End pre-defined quicksort


bool isAllUniqueChar2(string s)
{
	// if a stirng is longer than 256 or is None, return false
	if (s == "" || s.length() > 256)
	{
		return false;
	}

	string sorted_s = Randomized_QuickSort(s);
	for (int i = 0; i < sorted_s.length()-1; ++i)
	{
		if (sorted_s[i] == sorted_s[i+1])
		{
			return false;
		}
	}

	return true;
}


//=============================================================================================================================

int main()
{
	string s = "Hello, World!";
	cout<<"Method 1: "<<isAllUniqueChar(s)<<endl;
	cout<<"Method 2: "<<isAllUniqueChar2(s)<<endl;
	return 0;
}




