#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>

/**
 * infinite_while - creates an infinite loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - creates 5 zombie processes
 *
 * Return: 0 on success
 */
int main(void)
{
	int i, status;
	pid_t my_pid;

	for (i = 0; i < 5; i++)
	{
		my_pid = fork();
		if (my_pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", my_pid);
	}
	infinite_while();
	return (0);
}
