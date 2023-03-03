#include <iostream>
#include <string>
#include <cmath>
using namespace std;

//Задача 1
//За двома натуральними числами n і m визначити, чи можна n подати як суму двох натуральних доданків, а m – як суму їх квадратів.
//
//Наприклад, 10 = 7 + 3, 58 = 7 ^ 2 + 3 ^ 2 .
void ex1()
{
	int a = 0, b = 0, n, m;
	cout << "Enter natural number n: ";
	cin >> n;
	cout << "Enter natural number m: ";
	cin >> m;
	while (n <= 0 && m <= 0)
	{
		cout << "Error!" << endl;
		cout << "Enter first NATURAL number (>0): ";
		cin >> n;
		cout << "Enter second NATURAL number (>0): ";
		cin >> m;
	}
	while ((m != (a * a) + (b * b)) && a <= b)
	{
		a++;
		b = n - a;
	}
	if (a >= n)
	{
		cout << "The number n cannot be represented as the sum of two natural terms, and m - as the sum of their squares." << endl;
	}
	else
	{
		cout << "n = " << a << " + " << b << endl;
		cout << "m = " << a << "^2 + " << b << "^2" << endl;
	}
}

//Задача 2
//Потрібно з клавіатури ввести ціле число від 10 до 99. Якщо користувач набрав число за межами цього діапазону, то слід повторити спробу. 
//Отже, спочатку треба вводити число, а потім перевіряти умову того, що число є двозначним. (do - while)
void ex2()
{
	int a2;
	do
	{
		cout << "Enter natural number from 10 to 99: ";
		cin >> a2;
	} while (a2 < 10 || a2 > 99);
}

//Задача 3
//Написати програму, що знаходить добуток натуральних чисел у вказаному користувачем діапазоні.
void ex3()
{
	double min, max;
	do {
		cout << "Enter min natural number: ";
		cin >> min;
		cout << "Enter max natural number: ";
		cin >> max;
	} while (min > max);
	if (min < 0)
		min = 1;
	if (max < 0)
		max = 1;
	for (double i = min; i <= max; i++)
		min *= i;
	cout << min << endl;
}

//Задача 4
//Написати програму, що виводить на консоль таблицю множення на вказане користувачем число.
void ex4()
{
	double a;
	cout << "Enter number: ";
	cin >> a;
	for (size_t i = 1; i < 10; i++)
		cout << a << " * " << i << " = " << a * i << endl;
}

//Задача 5
//Написати функцію, що за цілим n>0 виводить на екран арифметичну прогресію. (a=1, d = 6)
void ex5()
{
	int a = 1, d = 6, n;
	cout << "Enter n of arithmetic progression: ";
	cin >> n;
	if (n <= 0)
		n = 1;
	for (size_t i = 1; i < n; i++)
	{
		cout << "a" << i << " = " << a << endl;
		a += d;
	}
	cout << "a" << n << " = " << a << endl;
}

//Задача 6
//Написати функцію, що за цілим числом визначає: 
//а) кількість цифр його десяткового запису;
//б) чи зустрічається в його десятковому запису задана цифра;
//в) кількість входжень заданої цифри в його десятковий запис;
//г) старшу цифру його десяткового запису;
//д) мінімальну(максимальну) цифру його десяткового запису.

int countDigit(int a)
{
	if (a / 10 == 0)
		return 1;
	return 1 + countDigit(a / 10);
}

void ex6()
{
	long long a;
	cout << "Enter integer: ";
	cin >> a;
	int* arr = new int[countDigit(a)];
	for (int i = countDigit(a); i > 0; i--) {
		arr[i - 1] = a % 10;
		a = a / 10;
	}

	#pragma region ex6_a
		int count = countDigit(a);
	#pragma endregion

	#pragma region ex6_b_c
		int b, is = 0;
		do {
			cout << "Enter integer (0 - 9): ";
			cin >> b;
		} while (b < 0 || b > 9);
		for (size_t i = 0; i < countDigit(a); i++)
		{
			if (b == arr[i])
				is++;
		}
	#pragma endregion

	#pragma region ex6_d
		int hd = arr[0];
	#pragma endregion

	#pragma region ex6_e
		int max = arr[0];
		int min = arr[0];
		for (size_t i = 0; i < countDigit(a); i++)
		{
			if (arr[i] > max)
			{
				max = arr[i];
			}
			else if (arr[i] < min)
			{
				min = arr[i];
			}
		}
	#pragma endregion
	
	#pragma region result
		cout << "The count of digits in your number: " << count << endl;
		if (is > 0)
			cout << "Whether the given digit is found in your number: True" << endl;
		else
			cout << "Whether the given digit is found in your number: False" << endl;
		cout << "The count of occurrences of a given digit in your number: " << is << endl;
		cout << "The higher digit of your number: " << hd << endl;
		cout << "Minimum digit in your number: " << min << endl;
		cout << "Maximum digit in your number: " << max << endl;
	#pragma endregion
	
}

int main()
{
	//ex1();
	//ex2();
	//ex3();
	//ex4();
	//ex5();
	//ex6();
}