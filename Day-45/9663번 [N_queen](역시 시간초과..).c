#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int n;
int* col;
int count;

void queen(int i) {
    if (promising(i)) {
        if (i == n) {
            printf("%d", count);
            return;
        }

        else {
            for (int j = 0; j < n; ++j) {
                col[i + 1] = j;
                queen(i + 1);
            }
        }
    }
}

int promising(int i) {
    int k = 1;
    while (k < i) {
        if (col[i] == col[k] || abs(col[i] - col[k]) == abs(i - k)) {
            return 0;
            k++;
        }
    }
    count++;
    return 1;
}

int main(void) {
    scanf("%d", &n);
    col = (int*)malloc(sizeof(int) * (n + 1));
    queen(0);
    free(col);
}