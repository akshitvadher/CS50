#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int len;
    do
    {
        get_int(" len of array :");
    }
    while (len < 1);

    int a[len];

    a[0]=1;
    printf("%i \n",a[0]);

    for (int i = 0 ; i < len ; i++)
    {
        a[i]= 2 * a[i-1];
        printf("%i \n",a[i]);
    }
}