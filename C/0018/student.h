#ifndef __STUDENT_H__
#define __STUDENT_H__

const int STR_LEN = 20;

typedef struct _student {
    char name[STR_LEN];
    int gender;
    int age;
} Student;

#endif
