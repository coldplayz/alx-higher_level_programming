#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * is_palindrome - checks if a list is a palindrome.
 * @head: address of pointer to the list head.
 *
 * Return: 1 if list is palindrome; 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	size_t i, len;
	int *pti;
	listint_t *temp;

	if (!head)
	{
		return (1);
	}
	len = listint_len(*head);
	if (len == 0)
	{
		return (1);
	}
	if (len % 2 != 0) /* odd list length */
	{
		return (0);
	}

	pti = malloc(sizeof(int) * (len / 2));
	if (!pti)
	{
		perror("malloc");
		return (0);
	}

	temp = *head;
	for (i = 0; i < (len / 2); i++) /* populate array of int */
	{
		/* At loop's end, temp will be pointing to the first struct */
		/* of the second half of the list */
		pti[i] = temp->n;
		temp = temp->next;
	}

	for (i = ((len / 2) - 1); temp; i--)
	{
		if (pti[i] != temp->n) /* compare potential palindrome values*/
		{
			return (0);
		}
		temp = temp->next;
	}
	free(pti);
	return (1);
}





/**
 * listint_len - determines the number of elements of the structure listint_s
 * @h: the head of a structure of type 'struct listint_s'
 *
 * Return: the number of nodes in the list
 */
size_t listint_len(const listint_t *h)
{
	size_t n = 0;
	listint_t *temp;

	temp = (listint_t *)h;
	for (; temp; temp = temp->next)
	{
		n++;
	}

	return (n);
}
