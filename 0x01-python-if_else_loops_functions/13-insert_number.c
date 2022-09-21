#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a new node in a sorted list.
 * @head: stores the address of the pointer to the first node
 * @n: integer to initialize new node with
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp, *temp2 = NULL;
	int i, list_len;

	list_len = listint_len(*head);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;

	temp = *head;  /* copy head so as not to modify the original */
	for (i = 0; temp; i++)
	{
		if (temp->n >= n)
		{
			if (temp == *head)
			{
				/* make 'new' the new head */
				new->next = *head;
				*head = new;
				break;
			}

			new->next = temp;
			temp2->next = new;
			break;
		}

		temp2 = temp;  /* temp2 saves current struct's pointer */
		temp = temp->next;  /* temp points to next struct */
	}
	
	if (i == list_len)  /* temp == NULL */
	{
		/* Insert at list end */
		/* temp2 is a pointer to the last struct node of the list */
		temp2->next = new;
		new->next = NULL;  /* 'new' now last node of list */
	}

	return (new);
}
