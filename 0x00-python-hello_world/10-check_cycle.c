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
	in int_struct = {0, 0, 1};
	st ptr_struct;

	if (list == NULL)
	{
		return (0);
	}

	ptr_struct.temp1 = list->next;
	/**
	 * temp1 stores the address of successive structs, starting
	 * from the struct head points to. temp2 stores the address
	 * of every struct from the head to temp1 (for each run of
	 * the second FOR loop), each of which is compared to temp1
	 * for equality. By the end of this loop, if 'flag' is set
	 * to zero, then temp2 would hold the address of the loop
	 * node, or there's no loop in the list.
	 */
	for (;; ptr_struct.temp1 = (ptr_struct.temp1)->next)
	{
		int_struct.n++;
		ptr_struct.temp2 = (listint_t *)list;
		for (int_struct.i = 0; int_struct.i < int_struct.n; int_struct.i++)
		{
			if (ptr_struct.temp2 == ptr_struct.temp1 || ptr_struct.temp1 == NULL)
			{
				int_struct.flag = 0;
				break;
			}
			ptr_struct.temp2 = (ptr_struct.temp2)->next;
		}
		if (int_struct.flag == 0)
			break;
	}
	if (ptr_struct.temp1 == NULL)
		return (0);
	else if (int_struct.flag == 0)
		return (1);
	return (1);
}
