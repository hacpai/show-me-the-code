#include <stdio.h>
#include "queue.h"

int main()
{
    Queue queue = init_queue();
    Elemtype num;
    do 
    {
        scanf("%d", &num);
        if (num != -1)
        {
            enqueue(&queue, num);
        }
    }
    while (num != -1);
    destory_queue(&queue);
    print_queue(&queue);

    return 0;
}

