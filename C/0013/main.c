#include <stdio.h>


int main()
{
    int result[200] = {0};
    int a, b;
    int i = 0;
    int count = 0;
    scanf("%d/%d", &a, &b);
    for (i = 0; i < 200; i++)
    {
        if (a < b)
        {
            a *= 10;
        }
        result[i] = a / b;
        count += 1;
        a = a % b;
        if ( a == 0)
        {
            break;
        }
    }
    printf("0.");
    for (int j = 0; j < count; j++)
    {
        printf("%d", result[j]);
    }
    printf("\n");
    return 0;
}
