#include <stdio.h>
typedef int T;


void swap(T* a, T* b)
{
    *a = *a ^ *b;
    *b = *a ^ *b;
    *a = *a ^ *b;
}

int bubble(T _elem[], int lo, int hi)
{
    int last = lo;
    while (++lo < hi)
    {
        if (_elem[lo-1] > _elem[lo])
        {
            last = lo;
            swap(&_elem[lo-1], &_elem[lo]);
        }
    }
    return last;
}

void bubbleSort(T _elem[], int lo, int hi)
{
    while (lo < bubble(_elem, lo, hi));
}


int main()
{
    T elem[10] = {6, 7, 3, 2, 7, 1, 5, 8, 7, 4};
    bubbleSort(elem, 0, 10);
    for (int i = 0; i < 10; i++)
    {
        printf("%d\t", elem[i]);
    }
    return 0;
}
