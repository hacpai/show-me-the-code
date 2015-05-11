#include <stdio.h>

typedef struct _point {
    int x;
    int y;
} Point;

void print_rect_coord(Point points[], int n);

int main()
{
    int n;
    scanf("%d", &n);
    Point points[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &points[i].x);
        scanf("%d", &points[i].y);
    }
    /*{*/
        /*for (int i = 0; i < n; i++)*/
        /*{*/
            /*printf("%d %d ", points[i].x, points[i].y);*/
        /*}*/
    /*}*/
    print_rect_coord(points, n);
    return 0;
}

void print_rect_coord(Point points[], int n)
{
    int min_x = points[0].x, min_y = points[0].y,
        max_x = points[0].x, max_y = points[0].y;
    for (int i = 1; i < n; i++)
    {
        if (min_x > points[i].x)
            min_x = points[i].x;
        if (min_y > points[i].y)
            min_y = points[i].y;
        if (max_x < points[i].x)
            max_x = points[i].x;
        if (max_y < points[i].y)
            max_y = points[i].y;
    }
    printf("%d %d %d %d", min_x, min_y, max_x, max_y);
}

