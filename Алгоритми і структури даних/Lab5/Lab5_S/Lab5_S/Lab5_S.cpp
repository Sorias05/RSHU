#include <iostream> 
using namespace std;

int n = 4;

//Згенерувати дві матриці розмірності 4 * 4 з відповідними назвами А та В.
//Заповнити їх випадковими числами в діапазоні від - 10 до 10 (або ініціалізувати вручну довільними зручними значеннями).
//
//Написати функції для виконання поставлених задач :
//-Обчислити суму відповідних елементів двох матриць А та В, записати результат у нову матрицю С та вивести її на екран.
//-Обчислити різницю відповідних елементів двох матриць А та В, записати результат у нову матрицю С та вивести її на екран.
//-Обчислити добуток двох матриць А та В, записати результат у нову матрицю С та вивести її на екран.
//-Обчислити визначник матриці А та вивести його на екран.

void randArray(int **arr, int row, int col)
{
    for (size_t i = 0; i < row; i++)
        for (size_t j = 0; j < col; j++)
            arr[i][j] = -10 + rand() % 21;
}

void printArray(int** arr, int row, int col)
{
    for (size_t i = 0; i < row; i++)
    {
        for (size_t j = 0; j < col; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

int** sumArray(int** arrA, int** arrB, int row, int col)
{
    int** arrC;
    arrC = new int* [row];
    for (int i = 0; i < row; i++)
        arrC[i] = new int[col];
    for (size_t i = 0; i < row; i++)
        for (size_t j = 0; j < col; j++)
            arrC[i][j] = arrA[i][j] + arrB[i][j];
    return arrC;
}

int** diffArray(int** arrA, int** arrB, int row, int col)
{
    int** arrC;
    arrC = new int* [row];
    for (int i = 0; i < row; i++)
        arrC[i] = new int[col];
    for (size_t i = 0; i < row; i++)
        for (size_t j = 0; j < col; j++)
            arrC[i][j] = arrB[i][j] - arrA[i][j];
    return arrC;
}

int** multArray(int** arrA, int** arrB, int row, int col)
{
    int** arrC;
    arrC = new int* [row];
    for (int i = 0; i < row; i++)
        arrC[i] = new int[col];

    for (size_t i = 0; i < row; i++)
        for (size_t j = 0; j < col; j++)
        {
            int mult = 0;
            for (size_t k = 0; k < row; k++)
                mult += arrA[i][k] * arrB[k][j];
            arrC[i][j] = mult;
        }
            
    return arrC;
}

int determinant(int** arr, int n)
{
    int det = 0;
    int** sArr;
    sArr = new int* [n];
    for (int i = 0; i < n; i++)
        sArr[i] = new int[n];

    if (n == 2)
        return ((arr[0][0] * arr[1][1]) - (arr[1][0] * arr[0][1]));
    else {
        for (int x = 0; x < n; x++) {
            int subi = 0;
            for (int i = 1; i < n; i++) {
                int subj = 0;
                for (int j = 0; j < n; j++) {
                    if (j == x)
                        continue;
                    sArr[subi][subj] = arr[i][j];
                    subj++;
                }
                subi++;
            }
            det = det + (pow(-1, x) * arr[0][x] * determinant(sArr, n - 1));
        }
    }
    
    return det;
}

int main()
{
    srand(time(0));
    int **A, **B, **C;
    A = new int* [n];
    B = new int* [n];
    C = new int* [n];
    for (int i = 0; i < n; i++)
    {
        A[i] = new int[n];
        B[i] = new int[n];
        C[i] = new int[n];
    }

    randArray(A, n, n);
    randArray(B, n, n);
    cout << "A:" << endl;
    printArray(A, n, n);
    cout << "B:" << endl;
    printArray(B, n, n);

    C = sumArray(A, B, n, n);
    cout << "A + B = " << endl;
    printArray(C, n, n);

    C = diffArray(A, B, n, n);
    cout << "A - B = " << endl;
    printArray(C, n, n);

    C = multArray(A, B, n, n);
    cout << "A * B = " << endl;
    printArray(C, n, n);

    cout << "Determinant A: " << determinant(A, n) << endl;

}
