#include <iostream>
using namespace std;

// Константи
const double d = 0.0108;
const int W = 50, H = 50;

// 1 спосіб
void firstWay()
{
    double N, M = 0, w, h, l, m, n = 0; // Створення змінних
    char c = ' ';

    cout << "Enter max kilograms: ";
    cin >> N;  // Вмістимість трюму
    double Nm = N / 100 * 90; // 90% вмістимості трюму

    cout << "\nConveyer window dimensions:\nWidth: " << W << " cm\nHeight: " << H << " cm\n";

    do
    {
        cout << "\nEnter width, height and length of gold bar in cm (w h l): ";
        cin >> w >> h >> l; // Розміри золотого злитку
        m = (w * h * l) * d; // Маса золотого злитку

        cout << "\nGold bar dimensions:\nWidth: " << w << " cm;\nHeight: " << h << " cm;\nLength: " << l << " cm.\n";
        cout << "Gold bar mass: " << m << " kg.\n\n";

        if (((w <= W && h <= H) || (h <= W && l <= H) || (w <= W && l <= H)) && (m + M) <= N) // Перевірка чи може цей золотий злиток пройти через вікно конвеєра або поміститись в трюм
        {
            M += m;
            cout << "This gold bar has entered the hold.\nThe hold is filled: " << M << "/" << N << endl << endl;
        }
        else
        {
            if (M >= Nm)
                n++;
            cout << "This gold bar cannot enter the hold." << M << "/" << N << endl << endl;
        }

        if (M >= N) // Перевірка чи трюм вже досить повний, щоб сказати користувачу "допобачення" 
            cout << "The hold is full! Have a good day :)" << endl;
        else if (n >= 3) // Перевірка чи користувач вже перевищив норму не вдалих спроб помістити злиток, щоб сказати йому "допобачення" 
            cout << "It is enough for you! Have a good day :)" << endl;
        else
        {
            cout << "Enough?(y/n): ";
            cin >> c;
        }

    } while ((M <= N) && (n < 3) && (c != 'y' && c != 'Y')); // Цикл до того моменту, поки трюм не буде досить повним, поки користувач не перевищить норму не вдалих спроб помістити злиток, поки користувач не скаже "досить"

    if (c == 'y' || c == 'Y') // Перевірка чи користувач сказав "досить", щоб сказати йому "допобачення"
        cout << "\Have a good day :)" << endl;
}

// 2 спосіб
void secondWay()
{
    srand(time(0)); // Створення випадковості в програмі

    double N, M = 0, w, h, l, m, n = 0; // Створення змінних
    char c = ' ';

    cout << "Enter max kilograms: ";
    cin >> N;  // Вмістимість трюму
    double Nm = N / 100 * 90; // 90% вмістимості трюму

    cout << "\nConveyer window dimensions:\nWidth: " << W << " cm\nHeight: " << H << " cm\n";

    do
    {
        // Розміри золотого злитку
        w = 1 + rand() % 100;
        h = 1 + rand() % 100;
        l = 1 + rand() % 100;
        m = (w * h * l) * d; // Маса золотого злитку

        cout << "\nGold bar dimensions:\nWidth: " << w << " cm;\nHeight: " << h << " cm;\nLength: " << l << " cm.\n";
        cout << "Gold bar mass: " << m << " kg.\n\n";

        if (((w <= W && h <= H) || (h <= W && l <= H) || (w <= W && l <= H)) && (m + M) < N) // Перевірка чи може цей золотий злиток пройти через вікно конвеєра або поміститись в трюм
        {
            M += m;
            cout << "This gold bar has entered the hold.\nThe hold is filled: " << M << "/" << N << endl << endl;
        }
        else
        {
            if (M >= Nm)
                n++;
            cout << "This gold bar cannot enter the hold.\nThe hold is filled: " << M << "/" << N << endl << endl;
        }

        if (M >= N) // Перевірка чи трюм вже досить повний, щоб сказати користувачу "допобачення" 
            cout << "The hold is full! Have a good day :)" << endl;
        else if (n >= 10) // Перевірка чи користувач вже перевищив норму не вдалих спроб помістити злиток, щоб сказати йому "допобачення" 
            cout << "It is enough for you! Have a good day :)" << endl;
        else
        {
            cout << "Enough?(y/n): ";
            cin >> c;
        }

    } while ((M <= N) && (n < 10) && (c != 'y' && c != 'Y')); // Цикл до того моменту, поки трюм не буде досить повним, поки користувач не перевищить норму не вдалих спроб помістити злиток, поки користувач не скаже "досить"

    if (c == 'y' || c == 'Y') // Перевірка чи користувач сказав "досить", щоб сказати йому "допобачення"
        cout << "\Have a good day :)" << endl;
}

int main()
{
    cout << "<<<<<<<<<< Conveyer >>>>>>>>>>" << endl << endl;
    //firstWay();
    secondWay();
}
