#include <iostream>
using namespace std;

void rand2DArray(int** arr, int row, int col)
{
    for (size_t i = 0; i < row; i++)
        for (size_t j = 0; j < col; j++)
            arr[i][j] = rand() % 100;
}

void print2DArray(int** arr, int row, int col)
{
    for (size_t i = 0; i < row; i++)
    {
        for (size_t j = 0; j < col; j++) {
            cout << arr[i][j] << "  ";
        }
        cout << endl;
    }
    cout << endl;
}

void printArray(int arr[], int row, int col)
{
    for (size_t i = 0; i < row; i++)
    {
        cout << arr[i] << "  ";
    }
    cout << endl;
}

//Порахувати кількість парних чисел у кожному рядку матриці.

int* evenCountArray(int** arr, int row, int col)
{
    int *countArr = new int [row];
    for (size_t i = 0; i < row; i++)
    {
        int count = 0;
        for (size_t j = 0; j < col; j++) {
            if (arr[i][j] % 2 == 0)
                count++;
        }
        countArr[i] = count;
    }
    return countArr;
}

int main()
{
    srand(time(0));
    int s;
    int** arr;

    cout << "Enter size of matrix: ";
    cin >> s;

    arr = new int* [s];
    for (int i = 0; i < s; i++)
        arr[i] = new int[s];

    rand2DArray(arr, s, s);
    print2DArray(arr, s, s);

    printArray(evenCountArray(arr, s, s), s, s);
}
