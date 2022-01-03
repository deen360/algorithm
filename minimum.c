#include <cs50.h>
#include <stdio.h>
#include <string.h>


float minimum(int s, float array[]);

int main (void)


{


    float k[13] = {10, 20, 30, 5, 100 , 0.9, 4, 6, 7, 200, 2, 5, 2000};
    int y = 13;

      printf("minimum %f \n", minimum (y, k));

} 


float minimum (int n, float s[])
    {
        float min = s[1];
        for (int i=0;  i < n; i++)
        {
            if (s[i] < min)
            {
                min = s[i];
            }


        }
        return min;
    }
