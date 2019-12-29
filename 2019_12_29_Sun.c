#include <stdio.h>

int main(void)
{
  int cur = 2;
  int is = 0;
  
  whild (cur < 10) 
    {
      is = 1;
      
      while (is <10)
        {
        printf("%d X %d = %d", cur, is, cur * is);
        is ++;
        }
    cur ++;
    }
return 0; 
}
