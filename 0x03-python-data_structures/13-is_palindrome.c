#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @h: pointer to the first node
 *
 * Return: pointer to the first node of the new list
 */

void reverse_listint(listint_t **h)
{
	listint_t *prev = NULL;
	listint_t *curr = *h;
	listint_t *next = NULL;

	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*h = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *rev = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			rev = slow->next;
			break;
		}
		if (!fast->next)
		{
			rev = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&rev);

	while (rev && temp)
	{
		if (temp->n == rev->n)
		{
			rev = rev->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!rev)
		return (1);

	return (0);
}
