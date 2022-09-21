#include <stdio.h>
#include <stdlib.h>
#include "lists.h"




/**
 * check_cycle - returns the node on which a list's loop occurs, if any.
 * @head: the top of the list
 *
 * Return: 1 if loop exists; 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	int i, flag = 1, n = 0;
	listint_t *temp1;

	if (list == NULL)
	{
		return (0);
	}

	temp1 = list;
	while (1)
	{
		if (hash_srch(temp1))
		{
			return (1);
		}

		temp1 = temp1->next;
		if (!temp1)
		{
			return (0);
		}
	}

	return (0);
}


/**
 * hash_srch - aids in checking for list loops.
 * @st: pointer to listint_t struct.
 *
 * Description: helper to check_cycle(). NULL
 * st should be handled in the calling function.
 * Return: 1 if loop found; 0 otherwise.
 */
int hash_srch(listint_t *st)
{
	static listint_t *list[64];
	static int entry_cnt = 0, offset = 0;
	int i;

	if (entry_cnt == 0)
	{
		entry_cnt++;
		for (i = 0; i < 64; i++)
		{
			list[offset++] = NULL; /* init list */
		}
		list[0] = st;
		return (0); /* no duplicate yet */
	}

	for (i = 0; list[i]; i++)
	{
		if (st == list[i])
		{
			return (1);
		}
	}
	list[offset++] = st; /* add st to list */

	return (0);
}
