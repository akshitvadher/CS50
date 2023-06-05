#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int l=0;
    do
    {
        get_int(" l of array :");
    }
    while(l < 1);

    int a[l];


    a[0]=1;
    printf("%i \n",a[0]);

    for (int i = 1; i < l ; i++)
    {
        a[i]= 2 * a[i-1];
        printf("%i \n",a[i]);
    }
}