#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n = get_int(" size of array :");

    int a[n];

     for(int i = 0 ; i < n ; i++)
        {
            printf("\n %i", a[i]);
        }

}