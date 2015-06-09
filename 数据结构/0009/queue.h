#ifndef _QUEUE_H_
#define _QUEUE_H_

typedef int Elemtype;

typedef struct _node 
{
    Elemtype data;
    struct _node *next;
} Node;

typedef struct _queue
{
    Node *first;
    Node *rear;
    int length;
    int lock;
} Queue;

Queue init_queue();
void enqueue(Queue *q, Elemtype e);
void print_queue(Queue *q);
Node *get_head(Queue *q);
Node *dequeue(Queue *q);
void clear_queue(Queue *q);
void destory_queue(Queue *q);

#endif
