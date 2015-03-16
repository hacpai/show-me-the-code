#include <stdio.h>
#include <string.h>

#define LEN 80
char * mystrcat(char *dst, const char *src);

int main()
{
    char s1[LEN];
    char s2[LEN];
    scanf("%s %s", s1, s2);
    int substr_len = strlen(s2);
    char *p = NULL;
    while ((p = strstr(s1, s2)))
    {
        *p = '\0';
        p += substr_len;
        mystrcat(s1, p); 
    }
    printf("%s", s1);
    return 0;
}

char * mystrcat(char *dst, const char *src)
{
    char *ret = dst;
    while(*dst)
    {
        dst++;
    }
    while(*src)
    {
        *dst++ = *src++;
    }
    *dst = '\0';
    return ret;
}
