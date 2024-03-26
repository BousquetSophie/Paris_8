#include <stdio.h>
#include <stdlib.h>

int stock[20000];

int compareEntier(const void* pEntier1, const void* pEntier2)
{
  return ( *(int*)(pEntier1) - *(int*)(pEntier2) );
}

int triee(int v, int nb)
{
   int mid = nb/2;
   
   if(v > stock[mid])
   {
      for(int i = mid-1; i < nb; i++)
      {
         if(v == stock[i])
         {
            printf("%d\n", 1);
            return 1;
         }   
      }
   }
   else
   {
      for(int i = 0; i < nb; i++)
      {
         if(v == stock[i])
         {
            printf("%d\n", 1);
            return 1;
         }   
      }
   }
   
   printf("%d\n", 0);
   return 0;
}

int main()
{
    int nb_stock = 0;
    scanf("%d", &nb_stock);
    
    for(int i = 0; i < nb_stock; i++)
       scanf("%d", &(stock[i]));
       
    qsort(stock, nb_stock, sizeof(int), compareEntier);
       
    int nb_question = 0;
    scanf("%d", &nb_question);
    
    for(int i = 0; i < nb_question; i++)
    {
       int valeur = 0;
       scanf("%d", &valeur);
       triee(valeur, nb_stock);
    }
    
    return 0;
}
