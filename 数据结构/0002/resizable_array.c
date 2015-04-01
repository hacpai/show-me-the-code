#include <stdio.h>
#include <stdlib.h>
#include "resizable_array.h"

/*typedef struct {*/
    /*int size;*/
    /*int *array;*/
/*} Array;*/

int main()
{
    Array my_array = array_create(100);
    /*array_set(&my_array, 10, 10);*/
    int number = 0;
    int cnt = 0;
    while (number != -1)
    {
        scanf("%d", &number);
        if (number != -1)
            array_set(&my_array, cnt++, number);
    } 
    int val = array_get(&my_array, 10);
    printf("my_array's size=%d\n", array_size(&my_array));
    printf("my_array[10]=%d\n", val);
    array_free(&my_array);
    return 0;
}

Array array_create(int init_size)
{
    Array array;
    array.size = init_size;
    array.array = (int *)malloc(sizeof(int)*array.size);
    return array;
}

void array_free(Array *my_array)
{
    free(my_array->array);
    my_array->array = NULL;
    my_array->size = 0;
}

int array_size(const Array *my_array)
{
    return my_array->size;
}

int *array_at(Array *my_array, int index)
{
    if (index >= my_array->size)
    {
        array_inflate(my_array, 
                (index/BLOCK_SIZE+1)*BLOCK_SIZE-my_array->size);
    }
    return &(my_array->array[index]);
}

int array_get(Array *my_array, int index)
{
    return *array_at(my_array, index);
}

void array_set(Array *my_array, int index, int value)
{
    *array_at(my_array, index) = value;
}

void array_inflate(Array *my_array, int more_size)
{
    my_array->size += more_size;
    int *p = (int *)malloc(sizeof(int)*my_array->size);
    int i;
    for (i = 0; i < my_array->size; i++)
    {
        p[i] = my_array->array[i];
    }
    free(my_array->array);
    my_array->array = p;
}


