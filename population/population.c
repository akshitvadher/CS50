#include <stdio.h>
#include <cs50.h>

int main(void)
{

     // prompt of sstart llamas

     int start;

     do{

            start=get_int(" enter start : ");

     } while( start < 9);

     //prompt of end llamas

        int end;
     do{

            end=get_int(" enter end : ");

     } while( end < start);

     //how many yreas to reach the goal

     int year =0;

     while( start < end )
     {
         start += start /12 ;
         year++;

     }

     printf(" no of year  : %i \n",year);


}