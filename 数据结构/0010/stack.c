#include <stdio.h>
#include <stdlib.h>

typedef int Elemtype; 
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

int main()
{
    Stack stack = init_stack();
    Elemtype num;
    do
    {
        scanf("%d", &num);
        if (num != -1)
        {
            push_stack(&stack, num);
        }
    }
    while (num != -1);
    print_stack(&stack);
    int decimal_num, n_base_num;
    scanf("%d", &decimal_num);
    scanf("%d", &n_base_num);
    printf("%s", decimal_to_base_n(decimal_num, n_base_num));
    return 0;
}
   
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
        printf("%d\t", s->elements[i]);
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
    Elemtype ret = s->top;
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

