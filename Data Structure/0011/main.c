#include <stdio.h>
#include <stdlib.h>
#include "bitree.h"

int main()
{
    ElementType ch;
    BiTree bitree = init_bitree();
    char order[1024];
    scanf("%s", order);
    BiTNode *root = create_bi_sort_tree(&bitree, order);
    preorder_traverse(root);
    printf("\n");
    midorder_traverse(root);
    BiTNode *ret = delete_bitnode(&bitree, 'F');
    free(ret);
    printf("\n");
    postorder_traverse(root);
    printf("\n");
    return 0;
}

