#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a new node and linked list remains sorted
 * @head: the beginning of linked list
 * @number: value for n
 * Return: address of new node or NULL if fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *h = *head;
	unsigned int i = 0;

	if (!(h) || (*h).n > number)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);

		(*new).n = number;
		(*new).next = *head;

		*head = new;
		return (*head);
	}

	while (h)
	{
		if (!((*h).next) || (*h).next->n > number)
		{
			new = malloc(sizeof(listint_t));
			if (!new)
				return (NULL);

			(*new).n = number;
			(*new).next = (*h).next;
			(*h).next = new;
			return (new);
		}
		h = (*h).next;
		i++;
	}
	return (NULL);
}
