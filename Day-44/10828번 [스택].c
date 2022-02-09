#include <stdio.h>
#include <string.h>

int stack[100001];
int count = 0;

void push(int a) {
    stack[count] = a;
    count++;
}

void pop() {
    if (count != 0) {
        count--;
        printf("%d\n", stack[count]);
        stack[count] = 0;
    }

    else
        printf("%d\n", -1);
}

void size() {
    printf("%d\n", count);
}

void empty() {
    if (count != 0)
        printf("0\n");
    else
        printf("1\n");
}

void top() {
    if (count != 0) {
        printf("%d\n", stack[count - 1]);
    }

    else
        printf("%d\n", -1);
}

int main(void) {
    int n = 0;
    char word[10];

    scanf("%d", &n);

    for (int i = 0; i < n; ++i) {
        scanf("%s", &word);

        if (strcmp(word, "push") == 0) {
            int num;
            scanf("%d", &num);
            push(num);
        }

        else if (strcmp(word, "pop") == 0)
            pop();
        else if (strcmp(word, "size") == 0)
            size();
        else if (strcmp(word, "empty") == 0)
            empty();
        else if (strcmp(word, "top") == 0)
            top();
    }

    return 0;
}