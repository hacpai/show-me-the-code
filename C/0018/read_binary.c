#include <stdio.h>
#include "student.h"

void read(FILE *fp, int index);

int main()
{
    FILE *fp = fopen("student.data", "r");
    if (fp)
    {
        fseek(fp, 0L, SEEK_END);
        int size = ftell(fp);
        int number = size / sizeof(Student);
        int index;
        while (1)
        {
            printf("有%d个数据，你要看第几个：", number);
            scanf("%d", &index);
            if (index == -1)
                break;
            read(fp, index-1);
        }
        fclose(fp);
    }
    return 0;
}

void read(FILE *fp, int index)
{
    fseek(fp, sizeof(Student), SEEK_SET);
    Student aStu;
    if (fread(&aStu, sizeof(Student), 1, fp) == 1)
    {
        printf("第%d个学生：\n", index+1);
        printf("\t姓名：%s\n", aStu.name);
        printf("\t性别：");
        switch(aStu.gender)
        {
            case 0: printf("男\n"); break;
            case 1: printf("女\n"); break;
            case 2: printf("其他\n"); break;
        }
        printf("\t年龄：%d\n", aStu.age);
    }
}
