#include <stdio.h>
#include <cs50.h>

int main(void)
{

        int n;
     do{
         get_int(" size of array :");
       }
       while( n < 1);

    int a[n];

     for(int i = 0 ; i < n ; i++)
        {
            printf("\n %i", a[i]);
        }

}