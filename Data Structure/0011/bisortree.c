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

BiTNode *find_bitnode(BiTree *pTree, ElementType e)
{
    BiTNode *pNode = (BiTNode *)malloc(sizeof(BiTNode));
    pNode->data = e;
    pNode->lchild = NULL;
    pNode->rchild = NULL;
    BiTNode *p = pTree->root;
    while (p && pNode->data != p->data)
    {
        if (pNode->data > p->data)
        {
            p = p->rchild;
        }
        else
        {
            p = p->lchild;
        }
    }
    return p;
}
 
BiTNode *find_last_bitnode(BiTree *pTree, ElementType e)
{
    BiTNode *pNode = (BiTNode *)malloc(sizeof(BiTNode));
    pNode->data = e;
    pNode->lchild = NULL;
    pNode->rchild = NULL;
    BiTNode *p = pTree->root;
    BiTNode *last = NULL;
    while (p && pNode->data != p->data)
    {
        last = p;
        if (pNode->data > p->data)
        {
            p = p->rchild;
        }
        else
        {
            p = p->lchild;
        }
    }
    return last;
}

BiTNode *find_left_bitree_largest_bitnode(BiTNode *pNode)
{
    BiTNode *p = pNode->lchild;
    while (p->rchild)
    {
        p = p->rchild;
    }
    return p;
} 

BiTNode *find_right_bitree_littlest_bitnode(BiTNode *pNode)
{
    BiTNode *p = pNode->rchild;
    while (p->lchild)
    {
        p = p->lchild;
    }
    return p;
}

BiTNode *delete_leaf_bitnode(BiTree *pTree, BiTNode *current, BiTNode *last)
{
    last->lchild = last->rchild = NULL;
    return current; 
}

BiTNode *delete_degree_is_one_bitnode(BiTree *pTree, BiTNode *current, BiTNode *last)
{
    if (current->lchild)
    {
        if (last->lchild == current)
            last->lchild = current->lchild;
        else
            last->rchild = current->lchild;
    }
    else
    {
        if (last->lchild == current)
            last->lchild = current->rchild;
        else
            last->rchild = current->rchild;
    }
    return current;
}

BiTNode *delete_degree_is_two_bitnodes(BiTree *pTree, BiTNode *current, BiTNode *last)
{
    BiTNode *p = NULL;
    BiTNode *node = NULL;
    if (last->lchild == current)
    {
        node = find_right_bitree_littlest_bitnode(current);
    }
    else
    {
        node = find_left_bitree_largest_bitnode(current);
    }
    ElementType temp = node->data;
    BiTNode *penult = find_last_bitnode(pTree, temp);
    if (node->lchild || node->rchild)
    {
        p = delete_degree_is_one_bitnode(pTree, node, penult);
    }
    else
    {
        p = delete_leaf_bitnode(pTree, node, penult);
    }
    current->data = temp;
    return p;
}

BiTNode *delete_bitnode(BiTree *pTree, ElementType e)
{
    BiTNode *last = find_last_bitnode(pTree, e);
    BiTNode *current = find_bitnode(pTree, e);
    BiTNode *p = NULL;
    if (last)
    {
        if (current->lchild && current->rchild)
        {
            p = delete_degree_is_two_bitnodes(pTree, current, last);
        }
        else if (current->lchild || current->rchild)
        {
            p = delete_degree_is_one_bitnode(pTree, current, last);
        }
        else
        {
            p = delete_leaf_bitnode(pTree, current, last);
        }
    }
    else
    {
        if (current->lchild && current->rchild)
        {
            pTree->root = current->lchild;
            pTree->root->rchild = current->rchild;
        }
        else if (current->lchild || current->rchild)
        {
            if (current->lchild)
            {
                pTree->root = current->lchild;
                current->lchild = NULL;
            }
            else
            {
                pTree->root = current->rchild;
                current->rchild = NULL;
            }
        }
        else
        {
            pTree->root = NULL;
        }
        p = current;
    }
    return p;
}

