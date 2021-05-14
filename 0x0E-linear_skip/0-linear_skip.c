#include "search.h"

/**
 * linear_skip - Searches for a value in a sorted skip list of int
 * @list: Pointer to the head of the list
 * @value: Ponter on the first node where value is located
 *
 * Return: Pointer on success or NULL
 */

skiplist_t *linear_skip(skiplist_t *list, int value)
{
	skiplist_t *aux_express, *prev;

	aux_express = list->express;
	prev = list;
	if (list)
	{
		while (aux_express)
		{
			printf("Value checked at index [%lu] = [%d]\n",
			       aux_express->index, aux_express->n);
			if (!aux_express->express || aux_express->n >= value)
			{
				if (!aux_express->express && aux_express->n < value)
				{
					prev = aux_express;
					while (aux_express->next)
						aux_express = aux_express->next;
				}
				printf("Value found between indexes [%lu] and [%lu]\n",
				       prev->index, aux_express->index);
				while (prev)
				{
					printf("Value checked at index [%lu] = [%d]\n",
					       prev->index, prev->n);
					if (prev->n > value)
						return (NULL);
					if (prev->n == value)
						return (prev);
					prev = prev->next;
				}
				break;
			}
			prev = aux_express;
			aux_express = aux_express->express;
		}
		return (NULL);
	}
	else
		return (NULL);
}
