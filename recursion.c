#include <cs50.h>
#include <stdio.h>
#include  <math.h>


int factorial(int x);
int main(void)

{

   int x = get_int("input factorial number: ");

    printf("factorial is %i", factorial(x));

}



int factorial(int x)
{
    // checks if the number is less than 0
    if (x <= 0){

        return 0;
    };
    
    //checks if the number is equal to 1
    if (x == 1){

        return 1;
    }

    else
    {
        //calculated the factorial through recursion 
        return (x * factorial(x - 1));
    }

}
