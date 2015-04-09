#include <stdio.h>
#include <stdlib.h>
typedef int T;


void merge(T _elem[], int lo, int mi, int hi)
{
    int lb = mi - lo, lc = hi - mi;
    T* B = (T* )malloc(sizeof(T)*lb);
    for (int i = 0; i < lb; i++) B[i] = _elem[i+lo];
    T* C = _elem + mi;
    for (int i = lo, j = 0, k = 0; j < lb || k < lc;)
    {
        if (j < lb && (k >= lc || B[j] <= C[k])) _elem[i++] = B[j++];
        if (k < lc && (j >= lb || B[j] > C[k])) _elem[i++] = C[k++];
    }
    free(B);
}

void mergeSort(T _elem[], int lo, int hi)
{
    if (hi - lo < 2) return;
    int mi = (lo + hi) >> 1;
    mergeSort(_elem, lo, mi);
    mergeSort(_elem, mi, hi);
    merge(_elem, lo, mi, hi);
}

int main()
{
    T elem[19] = {53, 130, 120, 14, 206, 31, 380, 39, 402, 146, 491, 51, 54, 59, 722, 79, 82, 186, 92};
    mergeSort(elem, 0, 19);
    for (int i = 0; i < 19; i++)
        printf("%d\t", elem[i]);
    return 0;
}

