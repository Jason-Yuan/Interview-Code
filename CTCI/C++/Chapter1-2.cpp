#include <iostream>
#include <cstring>
#include <cstdlib>
#include <string>

using namespace std;

//=============================================================================================================================
//      Project:                  Chapter 1-2 
//      Ideas:                    Set two pointers points to the head and tail of the string respectively, then swap the value 
//                                that these two pointer points to, then both move toward to the center until meet each other.
//      Time Complexity:          O(n)
//      Space Complexity:         O(1)
//=============================================================================================================================

void Reverse(char* str)
{
	int start = 0;
	int end = 0;
	while (str[end] != '\0')
	{
		end++;
	}

	if (end == 0)
	{
		return;
	}

	end--; // more the end from '\0' to the last char

	while (start < end)
	{
		char tmp = str[start];
		str[start] = str[end];
		str[end] = tmp;
		start++;
		end--;
	}
}

//=============================================================================================================================

int main()
{
	char a[] = "Hello,World!";
	Reverse(a);
	cout<<"Reverse string: ";
	for (int i = 0; i < 12; ++i)
	{
		cout<<a[i]<<"";
	}
	cout<<endl;

	return 0;
}