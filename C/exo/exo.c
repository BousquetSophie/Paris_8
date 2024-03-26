#include<stdlib.h>
#include<stdio.h>
#include<assert.h>
#include<limits.h>

#define Debug(s) s
#define Drapeau printf("executions ligne %d\n",__LINE__);




typedef struct s_cellule_t{
   int val;
   struct s_cellule_t* suiv;
}cellule_t;

typedef cellule_t* Liste;


cellule_t* consL(int val,cellule_t* queue)
{
   cellule_t* c=(cellule_t*)malloc(sizeof *c );
   if(c==NULL) exit(1);
   c->val=val;
   c->suiv=queue;
   return c;
}



void libererL(cellule_t* l)
{

   cellule_t* t;
   while(l!=NULL)
   {
      t=l->suiv;
      free(l); 
      l=t;
   }
}
void afficherL(cellule_t* l)
{
   while(l!=NULL)
   {
      printf("%d ",l->val);
      l=l->suiv;
   }
   printf("<fin de liste>\n");
}

int longueurL(cellule_t* l)
{
   int cpt=0;
   while(l!=NULL)
   {
      l=l->suiv;
      cpt++;
   }
   return cpt;
}

int sommeL(cellule_t* l)
{
   int acc=0;
   while(l!=NULL)
   {
      acc+=l->val;
      l=l->suiv;
   }
   return acc;
}
int estTrieeL(cellule_t* l)
{

   int lv=INT_MIN;
   while(1)
   {
      if(l==NULL)
         return 1;
      if(l->val < lv)
         return 0;
      lv=l->val;
      l=l->suiv;
   }
}

void ajouteEnTeteL(int v,cellule_t** l)
{
   *l=consL(v,*l);
}

void fusionL(cellule_t** c,cellule_t** s)
{
   while(*c!=NULL)
      c=&(*c)->suiv;
   *c=*s;
   *s=NULL;
}

void insererL(int val, cellule_t** c,int i)
   // si i plus grand que la longueur de la liste insere en queue
{
   while(i>0 && *c!=NULL)
   {
      i--;
      c=&(*c)->suiv;
   }
   *c=consL(val,*c);
}

cellule_t* extraireL(cellule_t** li,int i)
   // si i plus grande que la longueur de la liste renvoie NULL
{
   cellule_t* t;
   while(i>0 && *li!=NULL)
   {
      i--;
      li=&(*li)->suiv;
   }
   t=*li;
   if(t!=NULL)
      *li=t->suiv;
   return t;
}

void insererTriee(int val,cellule_t** li)
{
   while(*li != NULL && val>(*li)->val) // la premiere condition doit apparaitre en premier
   {
      li=&(*li)->suiv;
   }
   *li=consL(val,*li);
}

void miroir(cellule_t** li)
{
   cellule_t* d=*li;
   cellule_t* t;
   cellule_t* a=NULL;
   while(d!=NULL)
   {
      t=d;
      d=d->suiv;
      t->suiv=a;
      a=t;
   }
   *li=a;
}



int main(void)
{
   cellule_t* li=NULL;
   insererTriee(3,&li);
   insererTriee(2,&li);
   insererTriee(5,&li);
   insererTriee(7,&li);
   insererTriee(2,&li);
   afficherL(li);
   miroir(&li);
   afficherL(li);
   free(extraireL(&li,2));
   afficherL(li);
   libererL(li);
   li=NULL;

   return EXIT_SUCCESS;
}


