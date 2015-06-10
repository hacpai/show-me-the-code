#ifndef _BITREE_H_
#define _BITREE_H_

typedef char ElementType;
typedef struct _bi_t_node {
    ElementType data;
    struct _bi_t_node *lchild, *rchild;
} BiTNode;

typedef struct _tree {
    BiTNode *root;
} BiTree;

BiTree init_bitree();
void insert_bi_sort_tree(BiTree *pTree, char *s);
BiTNode *create_bi_sort_tree(BiTree *pTree, char *s);
void access(BiTNode *pNode);
void preorder_traverse(BiTNode *pNode);
void midorder_traverse(BiTNode *pNode);
void postorder_traverse(BiTNode *pNode);
#endif
