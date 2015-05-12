#include <stdio.h>

typedef struct _fraction {
    int numerator;
    int denominator;
} Fraction;

Fraction create_fracti(int numerat, int demoninat);
int compare_fracti(Fraction *fracti1, Fraction *fracti2);
void print_compare_result(Fraction *fracti1, Fraction *fracti2,
        int compa_value);

int main()
{
    int a1, a2, b1, b2;
    Fraction a = create_fracti(a1, a2);
    Fraction b = create_fracti(b1, b2);
    int compa_value = compare_fracti(&a, &b);
    print_compare_result(&a, &b, compa_value);
    return 0;
}

Fraction create_fracti(int numerat, int demoninat)
{
    Fraction fracti;
    scanf("%d/%d", &numerat, &demoninat);
    fracti.numerator = numerat;
    fracti.denominator = demoninat;
    return fracti;
} 

int compare_fracti(Fraction *fracti1, Fraction *fracti2)
{
    int left_operand = fracti1->numerator * fracti2->denominator;
    int right_operand = fracti2->numerator * fracti1->denominator;
    if (left_operand > right_operand)
        return 1;
    else if (left_operand == right_operand)
        return 0;
    else
        return -1;
}

void print_compare_result(Fraction *fracti1, Fraction *fracti2,
        int compa_value)
{
    char compa_sign;
    switch (compa_value)
    {
        case -1:
            compa_sign = '<';
            break;
        case 0:
            compa_sign = '=';
            break;
        case 1:
            compa_sign = '>';
            break;
    }
    printf("%d/%d %c %d/%d", fracti1->numerator, fracti1->denominator,
            compa_sign, fracti2->numerator, fracti2->denominator);
}

