#include "lists.h"

/**
 * check_cycle - checks the linkedlist if contains a cycle
 * @list: head of linked list
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
		return (0);

	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}

	return (0);
}
