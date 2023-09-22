#include <iostream>
#include <vector>
using namespace std;

void Array()
{
    int size, max = 0;
    cout << "Enter size of array: ";
    cin >> size;
    double* arr = new double[size];
    cout << "Array: ";
    for (size_t i = 0; i < size; i++)
    {
        arr[i] = rand() % 1000;
        cout << arr[i] << " ";
    }
    cout << endl;
    for (size_t i = 0; i < size; i++)
    {
        if (arr[i] > max)
            max = arr[i];
    }
    cout << "Max: " << max << endl << endl;
}

void Vector()
{
    int size, max = 0;
    cout << "Enter size of array: ";
    cin >> size;
    vector<double> vect;
    for (size_t i = 0; i < size; i++)
    {
        vect.push_back(rand() % 1000);
        cout << vect[i] << " ";
    }
    cout << endl;
    for (size_t i = 0; i < vect.size(); i++)
    {
        if (vect[i] > max)
            max = vect[i];
    }
    cout << "Max: " << max << endl << endl;
}

int main()
{
    srand(time(0));
    Array();
    Vector();
}
