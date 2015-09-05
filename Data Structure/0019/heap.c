#include <stdio.h>
#define ElemType int

void swap(ElemType* l, ElemType* r) {
    *l ^= *r;
    *r ^= *l;
    *l ^= *r;
}

void minHeapFixup(ElemType heaps[], int n) {
    int parent = (n-1)/2;
    while (heaps[n] < heaps[parent] && parent >= 0) {
        swap(&heaps[n], &heaps[parent]);
        n = parent;
        parent = (n-1)/2;
    }
}

void minHeapAddElem(ElemType heaps[], int n, ElemType elem) {
   heaps[n] = elem;
   minHeapFixup(heaps, n);
}

void minHeapFixdown(ElemType heaps[], int start, int end) {
    int root = start;
    int child = 2*start+1;
    while (child < end) {
        if (child+1 < end && heaps[child] > heaps[child+1]) {
            child++;
        }
        if (heaps[child] < heaps[root]) {
            swap(&heaps[child], &heaps[root]);
            root = child;
            child = 2*root+1;
        }
        else 
            return;
    }
}
void minHeapDeleteElem(ElemType heaps[], int n) {
    heaps[0] = heaps[n-1];
    minHeapFixdown(heaps, 0, n-1);
}

void makeMinHeap(ElemType heaps[], int n) {
    for (int i = (n-2)/2 ; i >= 0; i--) {
        minHeapFixdown(heaps, i, n);
    }
}

int main() {
    ElemType valsToSort[] = {2, 1, 5, 6, 3, 4 };
#define VSIZE (sizeof(valsToSort)/sizeof(valsToSort[0]))
    makeMinHeap(valsToSort, VSIZE);
    printf("{");
    int ix;
    for (ix=0; ix<VSIZE; ix++) printf(" %d ", valsToSort[ix]);
    printf("}\n");
    return 0;
}

