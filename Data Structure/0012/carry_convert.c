#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

char *decimal_to_base_n(int decimal_num, int n);

int main()
{   
    int decimal_num, n_base_num;
    scanf("%d", &decimal_num);
    scanf("%d", &n_base_num);
    printf("%s", decimal_to_base_n(decimal_num, n_base_num));
    return 0;
}

char *decimal_to_base_n(int decimal_num, int n)
{
    Stack stack = init_stack();
    while (decimal_num)
    {
        push_stack(&stack, decimal_num % n);
        decimal_num = decimal_num / n;
    }
    char *p = NULL;
    char *s = (char *)malloc(sizeof(char)*stack_length(&stack)+1);
    p = s;
    while(!is_stack_empty(&stack))
    {
        Elemtype e = pop_stack(&stack);
        if (e >= 0 && e <= 9)
        {
            *s++ = (e + '0');
        }
        else if (e >= 10 && e <= 15)
        {
            *s++ = (e - 10 + 'A');
        }
        *s = '\0';
    }
    return p;
}

