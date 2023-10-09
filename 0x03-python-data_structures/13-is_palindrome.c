#include "lists.h"

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the linked list.
 *
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 1 if list is a palindrome
 *         0 if it is not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	listint_t *first_half, *second_half;
	int is_palindrome = 1;

	slow = fast = *head;

	if (*head == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	second_half = reverse_list(slow);
	first_half = *head;

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	reverse_list(second_half);
	*head = first_half;

	return (is_palindrome);
}
