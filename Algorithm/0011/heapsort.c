#include <stdio.h>
#define ElemType double
#define SWAP(l, r) do{ ElemType t=l;l=r; r=t; }while(0)

void siftDown(ElemType heaps[], int start, int end) {
    int root = start;
    int child = 2*root+1;
    while (child < end && heaps[root] < heaps[child]) {
        if (child+1 < end && heaps[child] < heaps[child+1]) {
            child++;
        }
        if (heaps[root] < heaps[child]) {
            SWAP(heaps[root], heaps[child]);
            root = child;
            child = 2*root+1;
        }
    }
}

void makeHeap(ElemType heaps[], int count) {
    for (int start = (count-2)/2; start >= 0; start--) {
        siftDown(heaps, start, count); 
    }
}

void heapsort(ElemType heaps[], int count) {
    makeHeap(heaps, count);
    for (int end = count-1; end > 0; end--) {
        SWAP(heaps[0], heaps[end]);
        siftDown(heaps, 0, end-1);
    }
}

int main() {
    ElemType heaps[] = {
        1.4, 50.2, 5.11, -1.55, 301.521, 0.3301, 40.17,
        -18.0, 88.1, 30.44, -37.2, 3012.0, 49.2 };
#define SIZE (sizeof(heaps)/sizeof(heaps[0]))
    heapsort(heaps, SIZE);
    printf("{ ");
    for (int i = 0; i < SIZE; i++) printf(" %.3f ", heaps[i]);
    printf(" }\n");
    return 0;
}
