#include <stdio.h>

void quicksort(int unsorted[], int n) {
    if (n < 2) return;
    int t, i, j, x;
    x = n/2;
    for (i = 0, j = n-1; ; i++, j--) {
        while (unsorted[i] < unsorted[x]) i++;
        while (unsorted[x] < unsorted[j]) j--;
        if (i >= j) break;
        t = unsorted[i];
        unsorted[i] = unsorted[j];
        unsorted[j] = t;
    }
    quicksort(unsorted, i);
    quicksort(unsorted + i, n - i);
}

int main() {
    int unsorted[] = { 72, 6, 57, 88, 60, 42, 83, 73, 48, 85 };
    int n = sizeof(unsorted) / sizeof(unsorted[0]);
    for (int i = 0; i < n; i++) {
        printf("%d%c", unsorted[i], i < n-1? ' ': '\n');
    }
    quicksort(unsorted, n);
    for (int i = 0; i < n; i++) {
        printf("%d%c", unsorted[i], i < n-1? ' ': '\n');
    }
}

