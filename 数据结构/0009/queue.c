#include <stdlib.h>
#include <stdio.h>
#include "queue.h"

Queue init_queue()
{
    Queue *q = (Queue *)malloc(sizeof(Queue));
    q->first = NULL;
    q->rear = NULL;
    q->length = 0;
    return *q;
}

void enqueue(Queue *q, Elemtype e)
{
    if (q)
    {
        Node *p = (Node *)malloc(sizeof(*p));
        p->data = e;
        p->next = NULL;

        if (q->first)
        {
            q->rear->next = p;
        }
        else
        {
            q->first = p;
        }
        q->rear = p;
        q->length++;
    }
}

void print_queue(Queue *q)
{
    Node *p = NULL;
    for (p = q->first; p; p=p->next)
    {
        printf("%d\t", p->data);
    }
    printf("\n");
}

Node *get_head(Queue *q)
{
    Node *p = NULL;
    if (q)
    {
        p = q->first;
    }
    return p;
}

Node *dequeue(Queue *q)
{
    Node *p = get_head(q);
    if (p)
    {
        q->first = p->next;
        p->next = NULL;
        if (q->first == q->rear)
        {
            q->rear = NULL;
        }
        q->length--;
    }
    return p;
}

void clear_queue(Queue *q)
{
    for (Node *p = dequeue(q); p; p = dequeue(q))
    {
        free(p);
    }
    q->first = NULL;
    q->rear = NULL;
}

void destory_queue(Queue *q)
{
    clear_queue(q);
    free(q);
}

