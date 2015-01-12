#include <stdio.h>
int main() {
    int k;
    scanf("%d", &k);
    int A[k];
    int l, r;
    int temp = 0;
    int sum;
    int thisSum=0, maxSum=-1;
    for (int i=0; i<k; i++) {
        scanf("%d", &A[i]);
        thisSum += A[i];
        if (thisSum > maxSum) {
            maxSum = thisSum;
            l = temp;
            r = i;
        } else if (thisSum < 0) {
            thisSum = 0;
            temp = i+1;
        }
    }
     
    sum = maxSum;
    if (sum == -1) {
        l = 0;
        r = k-1;
        sum = 0;
    }
    printf("%d %d %d", sum, A[l], A[r]); 
    return 0;
}
