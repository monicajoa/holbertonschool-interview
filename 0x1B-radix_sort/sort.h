#ifndef _SORT_H_
#define _SORT_H_

/*Librarys standars*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*Prints an array and list of integers*/
void print_array(const int *array, size_t size);

void radix_sort(int *array, size_t size);

#endif /* !_SORT_H_*/
