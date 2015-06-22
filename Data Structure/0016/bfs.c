#include "../0013/graph.h"
#include "../0009/queue.h"
#include <stdlib.h>

int visted_vex[MAX_VEX] = {0};

void breadth_first_search(Graph *g, int vex_index)
{
    Queue queue = init_queue();
    access(g->vex[vex_index]);
    enqueue(&queue, vex_index);
    while (!is_empty(&queue))
    {
        Node *p = dequeue(&queue); 
        int index = p->data;
        for (int i = find_adj_vex(g, vex_index, 0); i > -1; i = find_adj_vex(g, vex_index, i+1))
        {
            if (visted_vex[i] == 0)
            {
                access(g->vex[i]);
                enqueue(&queue, i);
                visted_vex[i] = 1;
            }
        }
        free(p);
    }
}

void breadth_first_search_traverse(Graph *g)
{
    for (int i = 0; i < g->vexnum; i++)
    {
        if (visted_vex[i] == 0)
        {
            breadth_first_search(g, i);
        }
    }
}

int main()
{
    Graph g = init_graph();
    display_graph(&g);
    breadth_first_search_traverse(&g);
    return 0;
}
