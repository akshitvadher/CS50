#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int lenth;
    do
    {
        get_int(" lenth of array :");
    }
    while (lenth < 1);

    int a[lenth];

    a[0]=1;
    printf("%i \n",a[0]);

    for (int i = 0 ; i < lenth ; i++)
    {
        a[i]= 2 * a[i-1];
        printf("%i \n",a[i]);
    }
}