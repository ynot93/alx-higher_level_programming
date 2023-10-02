#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: Pointer to traverse the list.
 *
 * Return: 1 if cycle is found,
 *         0 if not.
 */
int check_cycle(listint_t *list)
{
	const listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
