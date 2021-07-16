#include "lists.h"
/**
 * find_listint_loop - Check if there is a cycle in a linked list
 * @head: linked list head
 *
 * Return: address of the pointer where the cycle is
 */
listint_t *find_listint_loop(listint_t *head)
{
	listint_t *temp = head;
	listint_t *curr = head;
	while (temp != NULL && temp->next != NULL)
	{
		curr = curr->next;
		temp = temp->next;
		temp = temp->next;
		if (temp == curr)
		{
			return (temp);
		}
	}
	return (NULL);
}
