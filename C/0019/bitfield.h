#ifndef __BITFIELD_H__
#define __BITFIELD_H__

typedef struct  {
    unsigned leading: 3;
    unsigned FLAG1: 1;
    unsigned FLAG2: 1;
    unsigned trailing: 27;
} Bitfield;

#endif
