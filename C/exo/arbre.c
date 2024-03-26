#include<stdlib.h>
#include<stdio.h>
#include<assert.h>

typedef struct s_noeud_t{
   int v;
   struct s_noeud_t* g;
   struct s_noeud_t* d;
}noeud_t;


noeud_t* consA(noeud_t* g,noeud_t* d,int etiquette)
{
   noeud_t* a=(noeud_t*)malloc(sizeof *a);
   if(a==NULL) exit(1);
   a->v=etiquette;
   a->g=g;
   a->d=d;
   return a;
}

void libererA(noeud_t* a)
{
   if(a==NULL)
      return;
   libererA(a->g);
   libererA(a->d);
   free(a);
}
void parcoursPref(noeud_t* a)
{
   if(a==NULL)
   {
      printf("NULL ");
      return;
   }
   printf("%d ",a->v);
   parcoursPref(a->g);
   parcoursPref(a->d);
}
void parcoursPost(noeud_t* a)
{
   if(a==NULL)
   {
      printf("NULL ");
      return;
   }
   parcoursPost(a->g);
   parcoursPost(a->d);
   printf("%d ",a->v);
}
void parcoursInfix(noeud_t* a)
{
   if(a==NULL)
      return;
   printf("( ");
   parcoursInfix(a->g);
   printf("%d ",a->v);
   parcoursInfix(a->d);
   printf(") ");
}


int taille(noeud_t* a)
{
   if(a==NULL) return 0;
   return 1+taille(a->g)+taille(a->d);
}

int nbFeuilles(noeud_t* a)
{
   if(a==NULL) return 0;
   if(a->g==NULL && a->d==NULL) return 1;
   return nbFeuilles(a->g)+nbFeuilles(a->d);
}
int max(int a,int b)
{
   return a>b?a:b;
}
int hauteur(noeud_t* a)
{
   if(a==NULL)
      return -1;
   return 1+max(hauteur(a->g),hauteur(a->d));
}

int estDans(noeud_t* a,int v)
{
   if(a==NULL)
      return 0;
   if(a->v==v)
      return 1;
   if(estDans(a->g,v))
      return 1;
   if(estDans(a->d,v))
      return 1;
   return 0;
}


void construirePref(noeud_t** a)
{
   int v;
   scanf("%d",&v);
   if(v==-1)
   {
      *a=NULL;
      return;
   }
   *a=consA(NULL,NULL,v);
   construirePref(&(*a)->g);
   construirePref(&(*a)->d);
}

int construirePrefT(noeud_t** a,int* tab)
{
   int v=*tab;
   if(v==-1)
   {
      *a=NULL;
      return 1;
   }
   *a=consA(NULL,NULL,v);
   v=1;
   v+=construirePrefT(&(*a)->g,tab+v);
   v+=construirePrefT(&(*a)->d,tab+v);
   return v;
}




int main(void)
{
   int T[11]={1,3,4,-1,-1,5,-1,-1,2,-1,-1};
   noeud_t* t=NULL;
   construirePrefT(&t,T);
   parcoursInfix(t);
   assert(estDans(t,5));
   assert(!estDans(t,6));
   libererA(t);
   return EXIT_SUCCESS;
}


