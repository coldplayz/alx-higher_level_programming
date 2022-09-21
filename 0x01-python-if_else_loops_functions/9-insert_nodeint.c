#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_nodeint_at_index - inserts a new node at a given position.
 * @head: stores the address of the pointer to the first node
 * @idx: the index to insert the node at, starting from 0
 * @n: integer to initialize new node with
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
	listint_t *new, *temp, *temp2;
	unsigned int i, list_len;

	list_len = listint_len(*head);
	if (idx > list_len)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;

	temp = *head;
	if (idx > 0)
	{
		for (i = 0; i < idx; i++)
		{
			/**
			 * By the end of this loop, temp2 will hold the address
			 * of the node before the index position, and temp will
			 * hold the address of the struct currently at the index position
			 */
			temp2 = temp;
			temp = temp->next;
		}
		temp2->next = new;	/* struct at temp2 now points to new... */
		new->next = temp;	/* new now points to struct at temp, which it displaced */
	}
	else if (idx == 0)		/* if first node is to be displaced by new */
	{
		*head = new;		/* new is now the head... */
		new->next = temp;	/* ...and new is pointing to the previous head */
	}
	return (new);
}
