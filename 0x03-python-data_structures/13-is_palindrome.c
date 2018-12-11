#include "lists.h"
#include <stdio.h>

void reverse_list(listint_t **head);
int list_equiv(listint_t *l1, listint_t *l2);

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 0 (not palindrome) 1 (is palindrome)
 */
int is_palindrome(listint_t **head)
{
	listint_t *skip_1, *skip_2, *prev_s1, *first_half, *second_half, *mid;

	/* linked lists of length 0 and 1 are palindromes by default */
	if (!head || !(*head) || !((*head)->next))
		return (1);

	first_half = skip_1 = skip_2 = prev_s1 = *head;
	second_half = mid = NULL;

	while (skip_1 && skip_2 && skip_2->next)
	{
		prev_s1 = skip_1;
		skip_1 = skip_1->next;
		skip_2 = skip_2->next->next;
	}
	if (skip_2 == NULL) /* Even # of nodes */
		second_half = skip_1;
	else /* odd number of nodes, there is a middle node */
	{
		mid = skip_1;
		second_half = skip_1->next;
	}
	prev_s1->next = NULL; /* null terminate first half */
	reverse_list(&second_half);

	if (list_equiv(first_half, second_half))
		return (1); /* equivalent lists, palindrome found */
	else
		return (0);
}

/**
 * list_equiv - checks if two linked lists contain identical data and are
 * the same length as each other
 * @l1: list one to compare to list two
 * @l2: list two to compare to list one
 *
 * Return: 1 (equivalent) 0 (not equal)
 */
int list_equiv(listint_t *l1, listint_t *l2)
{
	while (l1 || l2)
	{
		if (l1->n != l2->n || !l1 || !l2)
			return (0);
		if (l1)
			l1 = l1->next;
		if (l2)
			l2 = l2->next;
	}
	return (1);
}

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to head of linked list so we can modify it
 *
 * Return: always void, modifies head itself.
 */
void reverse_list(listint_t **head)
{
	listint_t *next = NULL, *prev = NULL, *cur;

	cur = *head;
	while (cur)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	*head = prev;
}
