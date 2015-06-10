#ifndef __RESIZABLE_ARRAY_H_
#define __RESIZABLE_ARRAY_H_

const int BLOCK_SIZE = 20;

typedef struct {
    int *array;
    int size;
} Array;

Array array_create(int init_size);
void array_free(Array *my_array);
int array_size(const Array *my_array);
int *array_at(Array *my_array, int index);
int array_get(Array *my_array, int index);
void array_set(Array *my_array, int index, int value);
void array_inflate(Array *my_array, int more_size);

#endif
