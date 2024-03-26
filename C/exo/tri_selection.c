#include <stdio.h>

int main()
{
   int nb_bacs = 0;
   scanf("%d", &nb_bacs);
   
   int tab[nb_bacs];
   for(int i = 0; i < nb_bacs; i++)
   {
      scanf("%d", &(tab[i]));
   }
   
   //truc de recherche
   int max = 0;
   int index = 0;
   for(int i = 0; i < nb_bacs;i++)
   {
      for(int j = 0; j <=  nb_bacs-1-i; j++)
      {
         if(tab[j] >= max)
         {
            index = j;
            max = tab[j];
         }
      }
      tab[index] = tab[nb_bacs-1-i];
      tab[nb_bacs-1-i] = max;
      
      max = 0;
      index = 0;
   }
   
   for(int i = 0; i < nb_bacs; i++)
   {
      printf("%d ", tab[i]);
   }
}
