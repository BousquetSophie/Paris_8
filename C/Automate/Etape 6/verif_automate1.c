#include <stdio.h>
#include <string.h>
#include <assert.h>

//crétion des différent état
#define Etat_debut 1
#define Etat_2 2
#define Etat_3 3
#define Etat_4 4
#define Etat_succes 5
#define Etat_erreur 6

int main()
{
	int x = 66;
	char tab[66] = {'B','S','Q','O','Q','O','S','B','Q','O','O','S','Q','B','B','B',
	'S','Q','Q','O','Q','B','S','O','Q','Q','B','Q','S','Q','B','Q',
	'O','O','Q','O','Q','O','Q','B','B','S','Q','Q','O','Q','S','O',
	'B','Q','O','Q','B','S','Q','Q','O','S','Q','S','O','B','S','Q',
	'Q','O'};
	
	// initialisation des valeurs à obtenir
	char tab_occ_obtenir[6][100] = {"BSQO","BBBSQQO","BSO","BBSQQO","BSQQO","BSQQO"};
	
	int tab_indice_obtenir[6][2]={{0,3},{13,19},{21,23},{39,44},{52,56},{61,65}};
	
	int nb_occ_obtenir = 6;
	
	
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
		else if ((etat_actuel == Etat_2) && (tab[i] == 'B'))
		{
			tab_verif[a] = 'B';
			a++;
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
		else if ((etat_actuel == Etat_3) && (tab[i] == 'O'))
		{
			tab_verif[a] = 'O';
			
			etat_actuel = Etat_succes;
		}
		else if ((etat_actuel == Etat_4) && (tab[i] == 'Q'))
		{
			tab_verif[a] = 'Q';
			a++;
		}
		else if ((etat_actuel == Etat_4) && (tab[i] == 'O'))
		{
			tab_verif[a] = 'O';
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
		else if (etat_actuel == Etat_erreur)
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
	printf("Motif 1 : B+SQ*O\n\n");
	printf("Tableau des occurences obtenu :\n\n");
	
	for(int z = 0; z <= nb_occ-1; z++)
	{
		printf("%s ", tab_occ[z]);
		printf("[%d  %d]\n", tab_indice[z][0], tab_indice[z][1]);
	}
	printf("\n");
	printf("Tableau des occurences à obtenir :\n\n");
	
	for(int y = 0; y <= nb_occ_obtenir-1; y++)
	{
		printf("%s ", tab_occ_obtenir[y]);
		printf("[%d  %d]\n", tab_indice_obtenir[y][0], tab_indice_obtenir[y][1]);
	}
	
	printf("\n");
	printf("Nombre d'occurence obtenu = %d\n", nb_occ);
	printf("Nombre d'occurence à obtenir = %d\n\n", nb_occ_obtenir);
	
	// assert pour vérification automatique
	
	assert(nb_occ == nb_occ_obtenir);
	
	for(int w=0; w<=nb_occ-1; w++)
	{
		assert(strcmp(tab_occ[w], tab_occ_obtenir[w]) == 0); 
		// on utilise strcmp car on peut pas utiliser des string avec assert
		// cela renvoie 0 si les deux string sont identique
		assert(tab_indice[w][0] == tab_indice_obtenir[w][0]);
		assert(tab_indice[w][1] == tab_indice_obtenir[w][1]);
	}
}
