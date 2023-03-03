#include <iostream>
#include <string>
#include <format>
#include <cmath>
using namespace std;

// Рівняння прямої
double eq(double xa, double ya, double xb, double yb, double xd, double yd)
{
	return ((xd - xa) * (yb - ya)) - ((xb - xa) * (yd - ya));
}

// Перевірка чи точка D i C лежать з одної сторони відносно прямої AB
bool isOnSameSide(double xa, double ya, double xb, double yb, double xc, double yc, double xd, double yd)
{
	return eq(xa, ya, xb, yb, xc, yc) * eq(xa, ya, xb, yb, xd, yd) > 0;
}

// Перевірка чи лежить точка на іншій точці
bool isOnPoint(double xa, double ya, double xd, double yd)
{
	return (xa == xd) && (ya == yd);
}

// Довжина вектора
double vLength(double xa, double ya, double xb, double yb)
{
	return sqrt((xb - xa) * (xb - xa) + (yb - ya) * (yb - ya));
}

// Перевірка чи точка D входить до проміжку
bool isBetween(double xa, double ya, double xb, double yb, double xd, double yd)
{
	return vLength(xa, ya, xb, yb) == (vLength(xa, ya, xd, yd) + vLength(xb, yb, xd, yd));
}

// Перевірка чи точка D належить стороні трикутника
bool isOnSide(double xa, double ya, double xb, double yb, double xd, double yd)
{
	return eq(xa, ya, xb, yb, xd, yd) == 0 && isBetween(xa, ya, xb, yb, xd, yd);
}

// Перетворення з double в string з 2 нулями після коми
string cToStr(double d)
{
	return to_string(d).substr(0, to_string(d).find(".") + 3);
}

int main()
{
	// Створення змінних
	double A[] = { 0,0 };
	double B[] = { -2,-2 };
	double C[] = { 0,-2 };
	double D[2];

	cout << "Triangle: \nA(" << A[0] << ";" << A[1] << ")\nB(" << B[0] << ";" << B[1] << ")\nC(" << C[0] << ";" << C[1] << ")" << endl;

	// Введіть координати точки D
	cout << "Enter point D(x; y): ";
	cin >> D[0] >> D[1];			

	string pD = ("D(" + cToStr(D[0]) + "; " + cToStr(D[1]) + ")");

	bool isInside = isOnSameSide(A[0], A[1], B[0], B[1], C[0], C[1], D[0], D[1]) && isOnSameSide(C[0], C[1], A[0], A[1], B[0], B[1], D[0], D[1]) && isOnSameSide(B[0], B[1], C[0], C[1], A[0], A[1], D[0], D[1]); // Перевірка чи точка D у трикутнику
	bool isOnTheSide = isOnSide(A[0], A[1], B[0], B[1], D[0], D[1]) || isOnSide(A[0], A[1], C[0], C[1], D[0], D[1]) || isOnSide(B[0], B[1], C[0], C[1], D[0], D[1]); // Перевірка чи належить точка D одній із сторін трикутника
	bool isOnThePoint = isOnPoint(A[0], A[1], D[0], D[1]) || isOnPoint(B[0], B[1], D[0], D[1]) || isOnPoint(C[0], C[1], D[0], D[1]); // Перевірка чи лежить точка D на одній із вершин трикутника

	// Результат
	cout << "The point " << pD << " is on another point of triangle : " << isOnThePoint << endl;
	cout << "The point " << pD << " is on side of triangle : " << isOnTheSide << endl;
	cout << "The point " << pD << " is inside of triangle : " << isInside << endl;
	cout << "The point " << pD << " is outside of triangle : " << !isInside << endl;
}


