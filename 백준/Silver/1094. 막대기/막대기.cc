
#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

int main() {
    int X;
    int stick;
    int i;
    int sum = 0;

    scanf("%d", &X);

    stick = 0;

    for (i = 64; i > 0; i /= 2) {

        if (i > X) {

            continue;

        }

        else if (i == X) {

            stick = 1;

            break;

        } if (sum + i <= X) {

            sum += i;

            stick++;

        }

    }

    printf("%d", stick);

    return 0;

}