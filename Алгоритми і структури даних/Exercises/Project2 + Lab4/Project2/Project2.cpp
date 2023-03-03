#include <iostream>
using namespace std;

const int s = 10;

void randArr(int arr[], int s, int min, int max)
{
	srand(time(0));
	for (size_t i = 0; i < s; i++)
	{
		arr[i] = min + rand() % max;
	}
}

void printArr(int arr[], int s)
{
	cout << "Array: ";
	for (size_t i = 0; i < s; i++)
	{
		cout << arr[i] << "   ";
	}
	cout << endl;
}

void bubbleSortArr(int arr[], int s)
{
	for (size_t i = 0; i < (s - 1); i++)
	{
		for (size_t j = 0; j < (s - 1); j++)
		{
			if (arr[j] > arr[j + 1])
			{
				int tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
			}
		}
	}
}

void choiceSortArr(int arr[], int s)
{
	int min = 0;
	for (int i = 0; i < s; i++)
	{
		min = i;

		for (int j = i + 1; j < s; j++)
			min = (arr[j] < arr[min]) ? j : min;

		if (i != min)
		{
			int tmp = arr[i];
			arr[i] = arr[min];
			arr[min] = tmp;
		}
	}
}

void insertionSortArr(int arr[], int s)
{
	for (int i = 1; i < s; ++i)
	{
		int j = i - 1;
		int tmp = arr[i];
		while (j >= 0 && tmp < arr[j])
		{
			arr[j + 1] = arr[j];
			arr[j] = tmp;
			--j;
		}
	}
}

void ex1()
{
	int arr[s];
	int target = 9;
	bool isTrue = false;

	randArr(arr, s, 0, 20);
	printArr(arr, s);
	bubbleSortArr(arr, s);
	//choiceSortArr(arr, s);
	//insertionSortArr(arr, s);
	printArr(arr, s);
	cout << endl;

	// 1 way
	/*for (size_t i = 0; i < (s); i++)
	{
		for (size_t j = 0; j < (s); j++)
		{
			if ((arr[i] + arr[j]) == target) {
				cout << "arr[" << i << "] + arr[" << j << "] = target" << endl;
				cout << arr[i] << " + " << arr[j] << " = " << target << endl;
				istrue = true;
			}
		}
	}*/

	// 2 way
	int l = 0, r = s - 1;
	while (l != r)
	{
		if (arr[l] + arr[r] == target)
		{
			cout << "arr[" << l << "] + arr[" << r << "] = target" << endl;
			cout << arr[l] << " + " << arr[r] << " = " << target << endl;
			isTrue = true;
			l++;
		}
		else if (arr[l] + arr[r] > target)
			r--;
		else
			l++;
	}

	cout << "\nIs any pair of values from array, which equals target = " << target << " ? " << isTrue << endl;
}

int main()
{
	ex1();
}
