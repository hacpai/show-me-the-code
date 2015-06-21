#include <stdio.h>
#include <stdlib.h>
#include "graph.h"

Graph* init_vertex(Graph *g)
{
    vertex vex[100];
    printf("Please input the vertex:" );
    scanf("%s", vex);
    vertex *p = vex;
    while (*p)
    {
        g->vex[g->vexnum++] = *p++;
    }
    return g;
}

int find_element(vertex vex[], int n, vertex x)
{
    int index = -1;
    for (int i = 0; i < n; i++)
    {
        if (vex[i] == x)
            index = i;
    }
    return index;
}

Graph* init_edge(Graph *g)
{
    vertex src, dest;
    weight w;
    for (int i = 0; i < g->vexnum; i++)
    {
        for (int j = 0; j < g->vexnum; j++)
        {
            g->w[i][j] = INF;
        }
    }
    printf("Please input the edge (format v1, v2, w): \n");
    do
    {
        scanf("%c, %c, %d", &src, &dest, &w);
        if (w != -1)
        {
            int row = find_element(g->vex, g->vexnum, src);  
            int col = find_element(g->vex, g->vexnum, dest);
            if (row != -1 && col != -1)
            {
                g->w[row][col] = w;
                g->edgnum++;
            }
        }
    } while (w != -1);
    return g;
}

Graph init_graph()
{
    Graph *g = (Graph *)malloc(sizeof(Graph));
    g->vexnum = 0;
    g->edgnum = 0;
    init_vertex(g);
    init_edge(g);
    return *g;
}

void display_graph(Graph *g)
{
    if (g)
    {
        for (int i = 0; i < g->vexnum; i++)
        {
            printf("%c\t", g->vex[i]);
        }
        printf("\n");
        for (int i = 0; i < g->vexnum; i++)
        {
            for (int j = 0; j < g->vexnum; j++)
            {
                printf("%d\t", g->w[i][j]);
            }
            printf("\n");
        }
    }
}

void access(vertex vex)
{
    printf("%c ", vex);
}

int find_adj_vex(Graph *g, int vex_index, int last_index)
{
    int index = -1;
    for (int col = last_index; col < g->vexnum; col++)
    {
        if (g->w[vex_index][col] < INF)
        {
            index = col;
            break;
        }
    }
    return index;
}

