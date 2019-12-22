#include <stdio.h> 
void main()
{
	//procedual programming
	int i = 1;
	int dan = 3;
	printf("[Procedual programming]");
	printf("[Gugudan %d Dan]\n", dan);

loop:
	printf("%2d x %2d = %2d\n", dan, i, dan * i);
	i++;
	if (i < 9) goto loop;
}
