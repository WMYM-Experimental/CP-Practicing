/*
Given two lists of integers, is there a set of numbers — one from each list — whose sum is equal to a specified value
*/

#include <iostream>
#include <vector>
using namespace std;

bool twoSum(vector<int> list, int value);

bool twoSum(vector<int> list, int value)
{
	for (int i = 0; i < list.size(); i++)
	{
		int diff = value - i;
		for (int j = i + 1; j < list.size(); j++)
		{
			if (list[j] == diff)
			{
				return true;
			}
		}
	}
	return false;
}