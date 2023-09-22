#include <iostream>
using namespace std;

// Швидке сортування
void QuickSort(int* arr, int a, int b)
{
    // Перевірка чи вже пройшлись по всьому масиву
    if (a >= b)
        return;

    int i = a, j = b, p = arr[a], count = 0; // Створення змінних

    // Знаходження кількості чисел які потрібно замінити
    for (int i = a + 1; i <= b; i++) {
        if (arr[i] <= p)
            count++;
    }

    // Надання опорному елементу його позиції
    int pIndex = a + count;
    swap(arr[pIndex], arr[a]);

    // Сортування правої і лівої частини від опорного елементу
    while (i < pIndex && j > pIndex) {
        while (arr[i] <= p) 
            i++;
        while (arr[j] > p) 
            j--;
        if (i < pIndex && j > pIndex)
            swap(arr[i++], arr[j--]);
    }
 
    QuickSort(arr, a, pIndex - 1); // Сортування тільки лівої частини
    QuickSort(arr, pIndex + 1, b); // Сортування тільки правої частини
}

int main()
{
    srand(time(0));

    // Створення динамічного одновимірного масиву
    int size;
    cout << "Enter size of array: ";
    cin >> size;
    int* arr = new int[size];

    // Присвоєння випадкових чисел масиву і його виведення в консоль
    cout << "Array: ";
    for (size_t i = 0; i < size; i++)
    {
        arr[i] = rand() % 100;
        cout << arr[i] << " ";
    }
    cout << endl;

    QuickSort(arr, 0, size-1); // Сортування

    // Виведення сортованого масиву в консоль
    cout << "Sorted array: ";
    for (size_t i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}
