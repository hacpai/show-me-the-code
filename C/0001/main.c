#include <stdio.h>

int main() {
    int bjt;
    scanf("%d", &bjt);
    int h = bjt / 100;
    int m = bjt % 100;
    int bjt_m = h*60 + m;
    int utc_m = bjt_m - 8*60;
    int utc;
    if (utc_m >= 0) {
        utc = utc_m / 60 * 100 + utc_m % 60;
    } else {
        utc = (utc_m + 24*60) / 60 * 100 + (utc_m + 24*60) % 60;
    }

    printf("%d", utc);
    
    return 0;

