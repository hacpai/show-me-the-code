#include <stdio.h>

typedef struct {
    int no;
    char name[20];
    int score1;
    int score2;
    int score3;
} Student;

Student * student_input(Student *pStudent);
double student_average(const Student *pStudent);
int student_get_score(const Student *pStudent, int index);
double student_get_average_score(const Student students[], int index);
int student_get_max_score(const Student students[], int index);
int student_get_min_score(const Student students[], int index);
void student_print(const Student *pStudent);

int main()
{
    Student student;
    Student students[10];
    for (int i = 1; i <= 10; i++)
    {
        students[i-1] = *student_input(&student);
        students[i-1].no = i;
    }
    printf("no\tname\tscore1\tscore2\tscore3\taverage\n");
    for (int i = 0; i < 10; i++)
    {
        student_print(&students[i]);
    }
    printf("\taverage\t%.2f\t%.2f\t%.2f\n", 
            student_get_average_score(students, 1),
            student_get_average_score(students, 2),
            student_get_average_score(students, 3));
    printf("\tmin\t%i\t%i\t%i\n", student_get_min_score(students, 1),
            student_get_min_score(students, 2),
            student_get_min_score(students, 3));
    printf("\tmax\t%i\t%i\t%i\n", student_get_max_score(students, 1),
            student_get_max_score(students, 2),
            student_get_max_score(students, 3));
    return 0;
}

int student_get_max_score(const Student students[], int index)
{
    int max = -1;
    for (int i = 0; i < 10; i++)
        if (student_get_score(&students[i], index) > max)
            max = student_get_score(&students[i], index);
    return max;
}

int student_get_min_score(const Student students[], int index)
{
    int min = 10;
    for (int i = 0; i < 10; i++)
        if (student_get_score(&students[i], index) < min)
            min = student_get_score(&students[i], index);
    return min;
}

double student_get_average_score(const Student students[], int index)
{
    double total = 0.0;
    for (int i = 0; i < 10; i++)
        total += student_get_score(&students[i], index); 
    return total/10;
}

void student_print(const Student *pStudent)
{
    printf("%i\t%s\t%i\t%i\t%i\t%f\n", pStudent->no, pStudent->name,
            pStudent->score1, pStudent->score2, pStudent->score3,
            student_average(pStudent));
}

int student_get_score(const Student *pStudent, int index)
{
    int score = 0;
    if (index == 1)
        score = pStudent->score1;
    if (index == 2)
        score = pStudent->score2;
    if (index == 3)
        score = pStudent->score3;
    return score;
}

double student_average(const Student *pStudent)
{
    return (pStudent->score1 + pStudent->score2 + pStudent->score3) / 3.0;
}

Student *student_input(Student *pStudent)
{ 
    printf("Enter a name: ");
    scanf("%s", pStudent->name);
    printf("Enter a score1: ");
    scanf("%i", &pStudent->score1);
    printf("Enter a score2: ");
    scanf("%i", &pStudent->score2);
    printf("Enter a score3: ");
    scanf("%i", &pStudent->score3);
    return pStudent;
}
