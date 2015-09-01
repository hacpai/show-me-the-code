#include <stdio.h>
typedef int T;


int interSearch(T _elem[], T e, int lo, int hi)
{
    while (lo < hi)
    {
        if (_elem[hi] != _elem[lo])
            int mi = (e - _elem[lo]) / (_elem[hi] - _elem[lo]) * (hi - lo) + lo;
        e < _elem[mi] ? hi = mi : (lo = mi + 1);
    }
    return --lo;
}


int main()
{
    T elem[19] = {5, 10, 12, 14, 26, 31, 38, 39, 42, 46, 49, 51, 54, 59, 72, 79, 82, 86, 92};
    printf("%d\n", interSearch(elem, 50, 0, 18));
    printf("%d\n", interSearch(elem, 51, 0, 18));
    printf("%d\n", interSearch(elem, 5, 0, 18));
    printf("%d\n", interSearch(elem, 92, 0, 18));
    printf("%d\n", interSearch(elem, 100, 0, 18));
    return 0;
}
