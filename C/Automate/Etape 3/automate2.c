#include<stdio.h>
#include <string.h>

//crétion des différent état
#define Etat_debut 1
#define Etat_2 2
#define Etat_3 3
#define Etat_4 4
#define Etat_5 5
#define Etat_succes 6
#define Etat_erreur 7

int main()
{
	int x = 200;
	char tab[200] = {'B','S','Q','O','Q','O','S','B','Q','O','O','S','Q','B','B','B',
	'S','Q','Q','O','Q','B','S','O','Q','Q','B','Q','S','Q','B','Q',
	'O','O','Q','O','Q','O','Q','B','B','S','Q','Q','O','Q','S','O',
	'B','Q','O','Q','B','S','Q','Q','O','S','Q','S','O','B','S','Q',
	'Q','O','B','O','Q','S','Q','B','S','Q','O','O','Q','S','S','Q',
	'Q','B','B','S','Q','O','Q','S','B','B','S','O','B','S','Q','S',
	'Q','O','O','B','B','S','O','S','Q','B','O','Q','O','Q','B','S',
	'Q','O','O','Q','O','Q','B','B','B','S','O','B','Q','O','Q','O',
	'O','B','S','O','S','B','Q','O','Q','B','B','B','B','S','Q','O',
	'B','S','Q','O','S','O','B','B','B','B','S','Q','Q','O','Q','B',
	'B','B','B','S','O','S','O','Q','Q','B','O','Q','S','B','S','Q',
	'O','O','Q','O','Q','Q','O','B','B','S','Q','O','S','Q','O','B',
	'O','Q','B','Q','O','Q','O','Q'};
	
//-------------------------------------------------------------------------------	
	
	//Tableau stockant les occurences
	char tab_occ[100][100];
	int ti = 0;
	
	int etat_actuel = 1;
	
	//tableau qui va stoker les lettres au fur et a mesure que on les valide
	char tab_verif[10] = {'X','X','X','X','X','X','X','X','X','X'};
	int a = 0;
	
	//Tableau stockant les indice de début et de fin
	int tab_indice[100][2];
	int indice_debut = 0;
	int indice_fin = 0;
	
	int nb_occ = 0; //nombre d'occurence
	
//-------------------------------------------------------------------------------
	
	int i = 0;
	while (i != x)
	{
		if ((etat_actuel == Etat_debut) && (tab[i] == 'B'))
		{
			tab_verif[a] = 'B';
			indice_debut = i;
			a++;
		
			etat_actuel = Etat_2;
		}
		else if ((etat_actuel == Etat_2) && (tab[i] == 'Q'))
		{
			tab_verif[a] = 'Q';
			a++;
			
			etat_actuel = Etat_4;
		}
		else if ((etat_actuel == Etat_2) && (tab[i] == 'S'))
		{
			tab_verif[a] = 'S';
			a++;
			
			etat_actuel = Etat_3;
		}
		else if ((etat_actuel == Etat_3) && (tab[i] == 'Q'))
		{
			tab_verif[a] = 'Q';
			a++;
			
			etat_actuel = Etat_4;
		}
		else if ((etat_actuel == Etat_4) && (tab[i] == 'O'))
		{
			tab_verif[a] = 'O';
			a++;
			
			etat_actuel = Etat_5;
		}
		else if ((etat_actuel == Etat_4) && (tab[i] != 'O'))
		{
			i--;
			etat_actuel = Etat_succes;
		}
		else if ((etat_actuel == Etat_5) && (tab[i] == 'O'))
		{
			tab_verif[a] = 'O';
		}
		else if ((etat_actuel == Etat_5) && (tab[i] != 'O'))
		{
			i--;
			etat_actuel = Etat_succes;
		}
		
		else
		{
			etat_actuel = Etat_erreur;
		}
	
		if (etat_actuel == Etat_succes)
		{
			indice_fin = i;
			tab_indice[ti][0] = indice_debut;
			tab_indice[ti][1] = indice_fin;
			nb_occ++;
			
			for(int j=0; j<=9; j++)
			{
				if(tab_verif[j] == 'B')
					strcat(tab_occ[ti],"B");
								
				else if(tab_verif[j] == 'S')
					strcat(tab_occ[ti],"S");
								
				else if(tab_verif[j] == 'Q')
					strcat(tab_occ[ti],"Q");
								
				else if(tab_verif[j] == 'O')
					strcat(tab_occ[ti],"O");
			}
			
			a = 0;
			indice_debut = 0;
			indice_fin = 0;
			ti++;
			etat_actuel = Etat_debut;
			
			for(int j=0; j<9; j++)
			{ 
				 tab_verif[j] = 'X';
			}
		}
		
		else if(etat_actuel == Etat_erreur)
		{
			a = 0;
			indice_debut = 0;
			indice_fin = 0;
			for(int j=0; j<9;j++)
			{
				 tab_verif[j] = 'X';
			}
			etat_actuel = Etat_debut;
			//printf("Modèle non conforme\n");
		}
		i++;
	}
	
	printf("Motif 2 : BS?QO*\n\n");
	printf("Affichage table des occurrences\n");
	
	for(int z = 0; z <= nb_occ-1; z++)
	{
		printf("%s", tab_occ[z]);
		printf(" [%d  %d]\n", tab_indice[z][0], tab_indice[z][1]);
	}
	
	printf("%d motifs 2 trouvés\n", nb_occ);
}
