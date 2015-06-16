#include <stdio.h>
#include <stdlib.h>

typedef char ElementType;

typedef struct _avl_node {
    ElementType elem;
    struct _avl_node *left;
    struct _avl_node *right;
    int height;
} AvlNode;
typedef AvlNode AvlTree;

/*typedef struct _avl_tree {*/
    /*AvlNode *root;*/
    /*int height;*/
    /*struct _avl_tree *left;*/
    /*struct _avl_tree *right;*/
/*} AvlTree;*/

AvlTree *init();
int height(AvlTree *t);
int max(int a, int b);
AvlTree *insert(AvlTree *t, ElementType x);
AvlTree *single_rotate_with_left(AvlTree *t);
AvlTree *single_rotate_with_right(AvlTree *t);
AvlTree *double_rotate_left_right(AvlTree *t);
AvlTree *double_rotate_right_left(AvlTree *t);

void preorder_traverse(AvlTree *pNode)
{
    if (pNode)
    {
        printf("%c", pNode->elem);
        preorder_traverse(pNode->left);
        preorder_traverse(pNode->right);
    }
}


int main()
{
    AvlTree *avltree = init();
    char *str = "ABCDEFG";
    char *p = str;
    while(*p)
    {
        avltree = insert(avltree, *p);
        p++;
    }
    preorder_traverse(avltree);
    return 0;
}

AvlTree* init()
{
    AvlTree *avltree = (AvlTree *)malloc(sizeof(AvlTree));
    /*avltree->root = NULL;*/
    avltree->height = 0;
    avltree->left = NULL;
    avltree->right = NULL;
    return avltree;
}

int height(AvlTree *t)
{
    if (t)
        return t->height;
    else
        return 0;
}

int max(int a, int b)
{
    return a > b? a : b;
}

AvlTree *insert(AvlTree *t, ElementType x)
{
    if (t)
    {
        if (x < t->elem)
        {
            t->left = insert(t->left, x);
            if (height(t->left) - height(t->right) == 2)
            {
                if (x < t->left->elem)
                    t = single_rotate_with_left(t);
                else
                    t = double_rotate_left_right(t);
            }
        }
        else if (x > t->elem)
        {
            t->right = insert(t->right, x);
            if (height(t->left) - height(t->right) == -2)
            {
                if (x > t->right->elem)
                    t = single_rotate_with_right(t);
                else
                    t = double_rotate_right_left(t);
            }
        }
    }
    else
    {
        t = (AvlTree *)malloc(sizeof(AvlTree));
        t->elem = x;
        t->left = NULL;
        t->right = NULL;
        /*t->root = p;*/
        t->height = 1;
        return t;
    }
    t->height = max(height(t->left), height(t->right)) + 1;
    return t;
}

AvlTree *single_rotate_with_left(AvlTree *t)
{
    AvlTree *p = t->left;
    t->left = p->right;
    p->right = t;
    t->height = max(height(t->left), height(t->right)) + 1;
    p->height = max(height(p->left), height(p->right)) + 1;
    return p;
}

AvlTree *single_rotate_with_right(AvlTree *t)
{
    AvlTree *p = t->right;
    t->right = p->left;
    p->left = t;
    t->height = max(height(t->left), height(t->right)) + 1;
    p->height = max(height(p->left), height(p->right)) + 1;
    return p;
}

AvlTree *double_rotate_left_right(AvlTree *t)
{
    t->left = single_rotate_with_right(t->left);
    AvlTree *p = single_rotate_with_left(t);
    return p;
}

AvlTree *double_rotate_right_left(AvlTree *t)
{
    t->right = single_rotate_with_left(t->right);
    return single_rotate_with_right(t);
}

