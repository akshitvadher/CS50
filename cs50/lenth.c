#include<stdio.h>
#include<cs50.h>

int main(void){

    string name = get_string("nam: ");

    int n =0;

    while( name[n] != '\0' )
    {
        n++;
    }
    printf("%i \n  ",n);
}