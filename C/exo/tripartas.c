#include<stdio.h>
#include<assert.h>

int fg(int a)
{
   return a*2+1;
}
int fd(int a)
{
   return a*2+2;
}
int pere(int a)
{
   return (a-1)/2;
}

int estUnTas(int n,int* t)
{
   int i;
   for(i=1;i<n;i++)
      if(t[pere(i)]>t[i])
         return 0;
   return 1;
   
}

void echange(int* a,int* b)
{
   int t;
   t=*a;
   *a=*b;
   *b=t;
}

void triParTas(int n,int* t)
{
   int j;
   int indMin;
   int tT; // taille du tas
   for(tT=2;tT<=n;tT++)
   {
      j=tT-1;
      while(j>0 && t[pere(j)]>t[j] )
      {
         echange(t+pere(j),t+j);
         j=pere(j);
      }
      assert(estUnTas(tT,t));
   }
   tT--;
   while(tT>1)
   {
      assert(estUnTas(tT,t));
      tT--;
      echange(t,t+tT);
      j=0;
      while(1)
      {
         if(fg(j)>=tT)
            break;
         if(fd(j)>=tT)
            indMin=fg(j);
         else
            indMin= t[fg(j)]>t[fd(j)] ? fd(j) : fg(j);

         if(t[j]<=t[indMin])
            break;
         echange(t+j,t+indMin);
         j=indMin;
      }
   }
}

int main(void)
{
   int T[11]={-3,6,-2,7,6,5,-4,6,-1,-2,-3};
   int i;
   triParTas(11,T);
   for(i=0;i<11;i++)
      printf("%d ",T[i]);
}
