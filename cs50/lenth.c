#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<ctype.h>

int main(void){

    string name = get_string("nam: ");

    int n= strlen(name);
    printf("\n %i ", n);

}