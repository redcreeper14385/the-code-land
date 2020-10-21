#include <stdio.h>


int main(void)

{
    int x;
    int y;
    printf("what would you like to add\n");
    scanf("%d%d", &x, &y); /*this makes it so you can input. 
                            gets() doesnt work*/

int z = y + x;
printf("%d", z);

return 0;

}