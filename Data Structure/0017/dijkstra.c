#include "../0013/graph.h"
#include <stdbool.h>
#include <stdio.h>

void init_dist_prev(Graph *g, int vex_index, weight dist[], int prev[])
{
    for (int i = 0; i < g->vexnum; i++)
    {
        dist[i] = g->w[vex_index][i];
        prev[i] = vex_index;
    }
}

int found_one_shortest_dist(Graph *g, bool found[], weight dist[])
{
    int shortest_dist = INF;
    int vex_index = -1;
    for (int i = 0; i < g->vexnum; i++)
    {
        if (!found[i] && dist[i] < shortest_dist)
        {
            shortest_dist = dist[i];
            vex_index = i;
        }
    }
    if (vex_index != -1)
        found[vex_index] = true;
    return vex_index;
}

void change_next_vex_path(Graph *g, int vex_index, bool found[], weight dist[], int prev[])
{
    for (int i = 0; i < g->vexnum; i++)
    {
        if (!found[i])
        {
            int tmp = (g->w[vex_index][i] == INF ? INF :
                    (g->w[vex_index][i] + dist[vex_index]));
            if (tmp < dist[i])
            {
                dist[i] = tmp;
                prev[i] = vex_index;
            }
        }
    }
}

void dijkstra_shortest_path(Graph *g, int vex_index, weight dist[], int prev[])
{
    bool found[MAX_VEX] = {false};
    init_dist_prev(g, vex_index, dist, prev);

    dist[vex_index] = 0;
    found[vex_index] = true;

    for (int i = 0; i < g->vexnum; i++)
    {
        int vex_index = found_one_shortest_dist(g, found, dist);
        change_next_vex_path(g, vex_index, found, dist, prev);
    }
}

void print_dijkstra_result(Graph *g, int vex_index, weight dist[], int prev[])
{
    printf("dijkstra(%c): \n", g->vex[vex_index]);
    for (int i = 0; i < g->vexnum; i++)
    {
        printf("Shortest(%c, %c) = %d %c", g->vex[vex_index], g->vex[i], dist[i], g->vex[i]);
        int j = i;
        do {
            printf("<-%c", prev[j]+'A');
            j = prev[j];
        } while (j != vex_index);
        printf("\n");
    }
}

int main()
{  
    Graph graph = init_graph();
    weight dist[MAX_VEX] = {INF};
    int prev[MAX_VEX] = {-1};
    display_graph(&graph);

    printf("Enter vextex index: ");
    int vex_index;
    scanf("%d", &vex_index);
    dijkstra_shortest_path(&graph, vex_index, dist, prev);
    print_dijkstra_result(&graph, vex_index, dist, prev);
    return 0;
}

