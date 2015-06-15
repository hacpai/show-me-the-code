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
void preorder_traverse_not_recur(BiTNode *pNode);
void midorder_traverse_not_recur(BiTNode *pNode);
void postorder_traverse_not_recur(BiTNode *pNode);
BiTNode *find_bitnode(BiTree *pTree, ElementType e);
BiTNode *find_last_bitnode(BiTree *pTree, ElementType e);
BiTNode *find_left_bitree_largest_bitnode(BiTNode *pNode);
BiTNode *find_right_bitree_littlest_bitnode(BiTNode *pNode);
BiTNode *delete_leaf_bitnode(BiTree *pTree, BiTNode *current, BiTNode *last);
BiTNode *delete_degree_is_one_bitnode(BiTree *pTree, BiTNode *current, BiTNode *last);
BiTNode *delete_degree_is_two_bitnodes(BiTree *pTree, BiTNode *current, BiTNode *last);
BiTNode *delete_bitnode(BiTree *pTree, ElementType e);

#endif
