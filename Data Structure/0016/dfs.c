#include "../0013/graph.h"

int visted_vex[MAX_VEX] = {0};

void deep_first_seach(Graph *g, int vex_index)
{
    visted_vex[vex_index] = 1;
    access(g->vex[vex_index]);
    for (int index = find_adj_vex(g, vex_index, 0); index > -1; index = find_adj_vex(g, vex_index, index+1))
    {
        if (visted_vex[index] == 0)
        {
            deep_first_seach(g, index);
        }
    }
}

void deep_first_seach_traverse(Graph *g)
{
    for (int i = 0; i < g->vexnum; i++)
    {
       if (visted_vex[i] == 0)
       {
           deep_first_seach(g, i);
       }
    }
}

int main()
{
    Graph g = init_graph();
    display_graph(&g);
    deep_first_seach_traverse(&g);
    return 0;
}

