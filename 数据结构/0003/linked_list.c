#include "node.h"
#include <stdio.h>
#include <stdlib.h>

/*typedef struct _node {*/
    /*int value;*/
    /*struct _node *next;*/
/*} Node;*/

typedef struct list {
    Node *head;
} List;

void add(List *pList, int number);
void print(List *pList);
void find(List *pList);
void del(List *pList);
void free_list(List *pList);

int main()
{
    int number;
    List list;
    list.head = NULL;
    do 
    {
        scanf("%d", &number);
        if (number != -1)
        {
            add(&list, number);
        }
    } while (number != -1);
    find(&list);
    del(&list);
    print(&list);
    free_list(&list);
    

    return 0;
}

void add(List *pList, int number)
{
    Node *p = (Node *)malloc(sizeof(Node));
    p->value = number;
    p->next = NULL;
    Node *last = pList->head;
    if (last)
    {
        while (last->next)
        {
            last = last->next;
        }
        last->next = p;
    }
    else
    {
        pList->head = p;
    }
}

void print(List *pList)
{
    Node *p = NULL;
    for (p = pList->head; p; p = p->next)
    {
        printf("%d\t", p->value);
    }
    printf("\n");
}

void find(List *pList)
{
    int number;
    scanf("%d", &number);
    Node *p = NULL;
    int isFound = 0;
    for (p = pList->head; p; p = p->next)
    {
        if (p->value == number)
        {
            printf("Found!\n");
            isFound = 1;
        }
    }
    if (!isFound)
    {
        printf("No Found!\n");
    }
}

void del(List *pList)
{
    Node *q = NULL;
    Node *p = NULL;
    int number;
    scanf("%d", &number);
    for (p = pList->head; p; q = p, p = p->next)
    {
        if (p->value == number)
        {
            if (q)
            {
                q->next = p->next;
            }
            else
            {
                pList->head = p->next;
            }
            free(p);
            break;
        }
    }
} 

void free_list(List *pList)
{
    Node *p = NULL;
    Node *q = NULL;
    for (p = pList->head; p; p = q)
    {
        q = p->next;
        free(p);
    }
}
