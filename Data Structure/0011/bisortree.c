#include <stdio.h>
#include <stdlib.h>
#include "bitree.h"

BiTree init_bitree()
{
    BiTree *bitree = (BiTree *)malloc(sizeof(BiTree));
    bitree->root = NULL;
    return *bitree;
}

BiTNode *create_bi_sort_tree(BiTree *pTree, char *s)
{
    while (*s)
    {
        insert_bi_sort_tree(pTree, s);
        s++;
    }
    return pTree->root;
}

void insert_bi_sort_tree(BiTree *pTree, char *s)
{
    BiTNode *p = (BiTNode *)malloc(sizeof(BiTNode));
    p->data = *s;
    p->lchild = NULL;
    p->rchild = NULL;

    BiTNode *current = pTree->root;
    BiTNode *last = NULL;
    if (current)
    {
        while (current)
        {
            last = current;
            if (p->data > current->data)
                current = current->rchild;
            else if (p->data < current->data)
                current = current->lchild;
            else
                break;
        }
        if (last->lchild == NULL && last->data > p->data)
            last->lchild = p;
        else if (last->rchild == NULL && last->data < p->data)
            last->rchild = p;
    }
    else
    {
        pTree->root = p;
    }
}

void access(BiTNode *pNode)
{
    printf("%c", pNode->data);
}

void preorder_traverse(BiTNode *pNode)
{
    if (pNode)
    {
        access(pNode);
        preorder_traverse(pNode->lchild);
        preorder_traverse(pNode->rchild);
    }
}

void midorder_traverse(BiTNode *pNode)
{
    if (pNode)
    {
        midorder_traverse(pNode->lchild);
        access(pNode);
        midorder_traverse(pNode->rchild);
    }
}

void postorder_traverse(BiTNode *pNode)
{
    if (pNode)
    {
        postorder_traverse(pNode->lchild);
        postorder_traverse(pNode->rchild);
        access(pNode);
    }
}

