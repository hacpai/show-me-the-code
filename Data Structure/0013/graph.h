#ifndef _GRAPH_H_
#define _GRAPH_H_

typedef char vertex;
typedef int weight;

#define INF 65535
#define MAX_VEX 100

typedef struct _graph {
    vertex vex[MAX_VEX];
    weight w[MAX_VEX][MAX_VEX];
    int vexnum;
    int edgnum;
} Graph;

Graph* init_vertex(Graph *g);
int find_element(vertex vex[], int n, vertex x);
Graph* init_edge(Graph *g);
Graph init_graph();
void display_graph(Graph *g);
void access(vertex vex);

#endif
