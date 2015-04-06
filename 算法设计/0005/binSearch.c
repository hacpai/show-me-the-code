#include <stdio.h>
typedef int T;


T binSearch(T _elem[], T e, int lo, int hi)
{
    while (lo < hi)
    {
        int mi = (hi+lo) >> 1;
        e < _elem[mi] ? hi = mi : (lo = mi + 1);
    }
    return --lo;
}

int main()
{
    T _elem[7] = {0, 1, 2, 3, 4, 5, 6};
    printf("%d\n", binSearch(_elem, 3, 0, 7));
    printf("%d\n", binSearch(_elem, 0, 0, 7));
    printf("%d\n", binSearch(_elem, 6, 0, 7));
    printf("%d\n", binSearch(_elem, 7, 0, 7));
    return 0;
}
