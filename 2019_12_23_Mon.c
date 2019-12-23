// 구구단
#include <stdio.h>

int main(void)
{
	int num = 0;
	int iter = 1;
	printf("Enter a number btw 2~ 9: ");
	scanf_s("%d", &num);
	while (iter < 10)
	{
		printf("%d x %d = %d \n", num, iter, num * iter);
		iter++;

	}
	return 0;
}
