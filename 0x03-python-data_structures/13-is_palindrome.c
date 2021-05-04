#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * count - counts elements in linked list
 * head: head of linked list
 * Return: number of elemments in linked list
 */

int count(listint_t **head)
{
	int n;
	const listint_t *current;
	current = *head;

	n = 0;
	while(current != NULL)
	{
		n++;
		current = current->next;
	}

	return (n);
}

/**
 * is_pal - check if int list is palindrome
 * start: check start
 * end: check end
 * list: list to check
 * Return: 1 if is palindrome else 0
 */

int is_pal(int start, int end, int *list)
{
	if (list[start] != list[end])
		return (0);
	else if (start >= end)
		return (1);
	else
		return (is_pal(++start, --end, list));
	return (0);
}

/**
 * is_palindrome - is palindrome set up
 * head: head of list
 * Return: 1 if is palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	int n;
	const listint_t *current;
	int elements = count(head);
	int *list = malloc(elements * sizeof(int));
	int start = 0;
	int end = elements - 1;
	int result;

	current = *head;
	n = 0;

	while (current != NULL)
	{
		list[n] = current->n;
		current = current->next;
		n++;
	}
	result = is_pal(start, end, list);

	free(list);
	return (result);

}
