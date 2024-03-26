#include <stdio.h>
#include <stdbool.h>
#define MAX_TAILLE 20
int nombresCarre[MAX_TAILLE][MAX_TAILLE];
int tailleGrille;

int totalPourDirection(int linDepart, int colDepart, int deltaLin, int deltaCol)
{
   int lin = linDepart, col = colDepart, total = 0;
   for (int position = 0; position < tailleGrille; position++)
   {
      total += nombresCarre[lin][col];
      lin += deltaLin;
      col += deltaCol;
   }
   return total;
}

bool totauxCorrects()
{
   int total = totalPourDirection(0, 0, 1, 1);
   
   if (totalPourDirection(0, tailleGrille - 1, 1, -1) != total)
      return false;
   
   for (int ligne = 0; ligne < tailleGrille; ligne++)
      if (totalPourDirection(ligne, 0, 0, 1) != total)
         return false;
   
   for (int colonne = 0; colonne < tailleGrille; colonne++)
      if (totalPourDirection(0, colonne, 1, 0) != total)
         return false;
   return true;
}

bool tousNombresPresents()
{
   int maxVal = tailleGrille * tailleGrille + 1;
   int nombrePresent[maxVal];
   for (int nombre = 0; nombre < maxVal; nombre++)
      nombrePresent[nombre] = 0;
   for (int ligne = 0; ligne < tailleGrille; ligne++)
      for (int colonne = 0; colonne < tailleGrille; colonne++)
      {
         int valeurCase = nombresCarre[ligne][colonne];
         if ((valeurCase <= 0) || (valeurCase >= maxVal))
            return 0;
         if (nombrePresent[valeurCase] != 0)
            return 0;
         nombrePresent[valeurCase]++;
      }
   return 1;
}

int main()
{
   scanf("%d", &tailleGrille);
   for (int ligne = 0; ligne < tailleGrille; ligne++)
      for (int colonne = 0; colonne < tailleGrille; colonne++)
         scanf("%d", &(nombresCarre[ligne][colonne]));
   if (tousNombresPresents() && totauxCorrects())
      printf("yes\n");
   else
      printf("no\n");
   return 0;
}
