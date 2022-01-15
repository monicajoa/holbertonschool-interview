#include "holberton.h"
#include <stdio.h>

/**
*wild_compare - Function to compare two strings
*@s1: First string
*@s2: Second string
*@ast: Flag for asterisk
*Return: integer
*/

int wild_compare(char *s1, char *s2, int ast)
{
	if (*s1 == '\0' && *s2 == '\0')
		return (1);
	if (*s2 == '*')
		return (wild_compare(s1, s2 + 1, ++ast));
	else if (*s1 != *s2 && ast > 0)
	{
		if (*s1 != '\0')
			return (wild_compare(s1 + 1, s2, ast));
		return (0);
	}
	else if (*s1 != *s2 && ast == 0)
		return (0);
	else if (*s1 == *s2 && ast > 0)
	{
		if (wild_compare(s1 + 1, s2 + 1, 0) == 1)
			return (wild_compare(s1 + 1, s2 + 1, ast));
		return (wild_compare(s1 + 1, s2, ast));
	}
	else if (*s1 == *s2 && ast == 0)
		return (wild_compare(s1 + 1, s2 + 1, 0));
	return (-1);
}

/**
*wildcmp - Function that compares two strings
*@s1: First string
*@s2: Second string
*Return: Returns 1 if the strings can be considered identical,
*otherwise return 0
*/

int wildcmp(char *s1, char *s2)
{
	int ast = 0;

	return (wild_compare(s1, s2, ast));
}
