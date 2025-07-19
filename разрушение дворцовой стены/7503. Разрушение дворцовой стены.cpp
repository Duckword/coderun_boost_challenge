// 7503. Разрушение дворцовой стены.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>

using namespace std;

long long solve(int n, std::vector<long long> a) {

    long long count = 0;
    vector<long long> cnt_max(n,0);
    vector<long long> cnt_min(n,0);
    stack <int> L_border;
    stack <int> R_border;

       //количество левых границ отрезка,где a[i] максимум

    for (int i = 0; i < n; i++) {

        while (!L_border.empty()) {
            if (a[i] > a[L_border.top()]) {
                L_border.pop();
            }
            else {
                break;
            };
        };
        
        if (!L_border.empty()) {
            cnt_max[i] = i - L_border.top();

        }
        else {
            cnt_max[i] = i+1;
        }
        L_border.push(i);
    };

    //количество правых границ,где a[i] максимум

    for (int i = n-1; i >-1; i--) {

        while (!R_border.empty()) {
            if (a[i] > a[R_border.top()]) {
                R_border.pop();
            }
            else {
                break;
            };
        };

        if (!R_border.empty()) {
            cnt_max[i] *= R_border.top() - i ;
        }
        else {
            cnt_max[i] *= n-i;
        }
        R_border.push(i);

    };

    //очистить стеки
    while (!L_border.empty()) {
        L_border.pop();
    }
    while (!R_border.empty()) {
        R_border.pop();
    }

    //количество левых границ отрезка где a[i] минимум 
    for (int i = 0; i < n; i++) {

        while (!L_border.empty()) {
            if (a[i] < a[L_border.top()]) {
                L_border.pop();
            }
            else {
                break;
            };
        };

        if (!L_border.empty()) {
            cnt_min[i] = i - L_border.top();

        }
        else {
            cnt_min[i] = i + 1;
        }
        L_border.push(i);
    };

    //количество правых границ отрезка где a[i] минимум 
    for (int i = n - 1; i > -1; i--) {

        while (!R_border.empty()) {
            if (a[i] < a[R_border.top()]) {
                R_border.pop();
            }
            else {
                break;
            };
        };

        if (!R_border.empty()) {
            cnt_min[i] *= R_border.top() - i;
        }
        else {
            cnt_min[i] *= n - i;
        }
        R_border.push(i);

    };

    //сумма максимумов
    for (int i = 0; i < n; i++) {
        count += cnt_max[i] * a[i];
    }
    //минус сумма минимумов
    for (int i = 0; i < n; i++) {
        count -= cnt_min[i] * a[i];
    }
    return count;
}
int main()
{

    
}

// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
