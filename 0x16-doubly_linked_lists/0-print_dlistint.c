#include "lists.h"
#include <stdio.h>

/**
 * print_dlistint - prints a doubly linked list
 * @h: head of doubly linked list (DLL)
 *
 * Return: number of nodes in DLL
 */
size_t print_dlistint(const dlistint_t *h)
{
	int nodes = 0;
	dlistint_t temp;

	if (!h)
		return (0);

	while (1)
	{
		printf("%d\n", temp.n);
		nodes++;
		if (temp.next == NULL)
			break;
		temp = *(temp.next);
	}
	return (nodes);
}
