#include <stdio.h>
#include "bitfield.h"

void prtBin(int n);

int main()
{
    Bitfield bit_field;
    bit_field.leading = 3;
    bit_field.FLAG1 = 1;
    bit_field.FLAG2 = 1;
    bit_field.trailing = 0;
    printf("sizeof(bit_field) = %lu\n", sizeof(bit_field));
    prtBin(*(int *)&bit_field);
    return 0;
}

void prtBin(int n)
{
    unsigned mask = 1u << 31;
    for (; mask; mask >>= 1)
        printf("%d", n & mask ? 1:0);
    printf("\n");
}
