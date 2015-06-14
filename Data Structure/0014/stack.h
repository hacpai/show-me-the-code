#ifndef _STACK_H_
#define _STACK_H_

#include "bitree.h"
#define Elemtype BiTNode*
#define STACK_MAX_SIZE 1024
typedef struct _seqstack 
{
    Elemtype elements[STACK_MAX_SIZE];
    int top;
} Stack; 
   
Stack init_stack();
void push_stack(Stack *s, Elemtype e);
void print_stack(Stack *s);
int stack_length(Stack *s);
int is_stack_empty(Stack *s);
int is_stack_full(Stack *s);
Elemtype get_top_stack(Stack *s);
Elemtype pop_stack(Stack *s);
void clear_stack(Stack *s);
void free_stack(Stack *s);
char *decimal_to_base_n(int decimal_num, int n);

#endif
