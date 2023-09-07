#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - ***
 * @list: ***
 * Return: ***
 */
int check_cycle(listint_t *list)
{
	listint_t *i = list, *x = list;

	while (x && x->next)
	{
		i = i->next;
		x = x->next->next;
		if (i == x)
			return (1);
	}
	return (0);
}
