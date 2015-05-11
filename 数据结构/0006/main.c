#include <stdio.h>
#include <stdlib.h>

typedef struct _node {
    char letter;
    struct _node *next;
    struct _node *prev;
} Node;

typedef struct _list {
    Node *head;
    Node *tail;
} List;

void add_string(List *string, char c);
void print_shift_right(List *string, int n);

int main()
{
    char c;
    int n;
    List string;
    string.head = NULL;
    string.tail = NULL;
    do
    {
        scanf("%c", &c);
        if (c != '#')
            add_string(&string, c);
    }
    while (c != '#');
    scanf("%d", &n);
    print_shift_right(&string, n);
    return 0;
}

void add_string(List *string, char c)
{
    Node *p = (Node *)malloc(sizeof(Node)); 
    p->letter = c;

    p->next = string->head;

    Node *last = string->tail;
    if (last)
    {
        string->head->prev = p;
        last->next = p;
        p->prev = last;
    }
    else
    {
        string->head = p;
    }
    string->tail = p;
}

void print_shift_right(List *string, int n)
{
    Node *p = string->tail;
    for (int i = 0; i < n-1; i++)
    {
        p = p->prev;
    }
    Node *temp = p;
    if (p)
    {
        for (; p->next != temp; p = p->next)
        {
            printf("%c", p->letter);
        }
        printf("%c", p->letter);
    }
}
