#include <stdio.h>

int main()
{
    int num;
    scanf("%d", &num);
    char readablility[][80] = {
        "",
        "unreadable",
        "barely readable, occasional words distinguishable",
        "readable with considerable difficulty",
        "readable with practically no difficulty",
        "perfectly readable",
    };
    char strength[][80] = {
        "",
        "Faint signals, barely perceptible",
        "Very weak signals",
        "Weak signals",
        "Fair signals",
        "Fairly good signals",
        "Good signals",
        "Moderately strong signals",
        "Strong signals",
        "Extremely strong signals",
    };
    if (num > 10 && num < 60)
    {
        printf("%s, %s.", strength[num%10], readablility[num/10]);
    }
    return 0;
}

