#include <stdio.h>
#include "stack.h"
#include "bitree.h"

void preorder_traverse_not_recur(BiTNode *pNode)
{
    Stack stack = init_stack();
    push_stack(&stack, pNode);
    BiTNode *p = NULL;
    while (pNode && !is_stack_empty(&stack))
    {
        p = pop_stack(&stack);
        access(p);
        if (p->rchild)
            push_stack(&stack, p->rchild);
        if (p->lchild)
            push_stack(&stack, p->lchild);
    }
}

void midorder_traverse_not_recur(BiTNode *pNode)
{
    Stack stack = init_stack();
    BiTNode *p = pNode;
    while (p != NULL || !is_stack_empty(&stack))
    {
        if (p)
        {
            push_stack(&stack, p);
            p = p->lchild;
        }
        else
        {
            p = pop_stack(&stack);
            access(p);
            p = p->rchild;
        }
    }
}

void postorder_traverse_not_recur(BiTNode *pNode)
{
    Stack stack = init_stack();
    BiTNode *p = pNode;
    push_stack(&stack, p);
    BiTNode *last = NULL;
    while (p && !is_stack_empty(&stack))
    {
        if (p->lchild)
        {
            p = p->lchild;
            push_stack(&stack, p);
        }
        else
        {
            p = get_top_stack(&stack);
            if (p->rchild && p->rchild != last)
            {
                p = p->rchild;
                push_stack(&stack, p);
            }
            else
            {
                last = pop_stack(&stack);
                access(last);
                p->lchild = NULL;
            }
        }
    }
}


int main()
{
    ElementType ch;
    BiTree bitree = init_bitree();
    char order[1024];
    scanf("%s", order);
    BiTNode *root = create_bi_sort_tree(&bitree, order);
    preorder_traverse_not_recur(bitree.root);
    printf("\n");
    midorder_traverse_not_recur(bitree.root);
    printf("\n");
    postorder_traverse_not_recur(bitree.root);
    printf("\n");
    return 0;
}
