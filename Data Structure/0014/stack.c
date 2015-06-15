#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

Stack init_stack()
{
    Stack *s = (Stack *)malloc(sizeof(Stack));
    s->top = -1;
    return *s;
}

void push_stack(Stack *s, Elemtype e)
{
    if (s->top == STACK_MAX_SIZE - 1)
    {
        printf("Stack is full.\n");
        exit(1);
    }
    s->elements[++s->top] = e;
}

void print_stack(Stack *s)
{
    for (int i = 0; i < stack_length(s); i++)
        printf("%c\t", s->elements[i]);
    printf("\n");
}

int stack_length(Stack *s)
{
    return s->top + 1;
}

int is_stack_empty(Stack *s)
{
    return s->top < 0;
}

int is_stack_full(Stack *s)
{
    return s->top >= STACK_MAX_SIZE - 1;
}

Elemtype get_top_stack(Stack *s)
{
    Elemtype ret = NULL;
    if (is_stack_empty(s))
    {
        printf("Stack is empty.");
        exit(1);
    }
    else 
    {
        ret = s->elements[s->top];
    }
    return ret;
}

Elemtype pop_stack(Stack *s)
{
    Elemtype ret;
    if (is_stack_empty(s))
    {
        printf("Stack is empty.\n");
        exit(1);
    }
    else 
    {
        ret = get_top_stack(s);
        s->top--;
    }
    return ret;
}

void clear_stack(Stack *s)
{
    s->top = -1;
}

void free_stack(Stack *s)
{
    clear_stack(s);
    free(s);
}

