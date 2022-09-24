#include <stdio.h>
#include <stdlib.h>
#include "lists.h"




/**
 * check_cycle - returns the node on which a list's loop occurs, if any.
 * @list: the top of the list
 *
 * Return: 1 if loop exists; 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_p = list, *fast_p = list;

	
	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
		{
			return 1;
		}
	}

	return 0;
}
