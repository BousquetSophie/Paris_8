#include <stdio.h>
#include <string.h>

//crétion des différent état

//Automate 1:
#define Etat1_debut 1
#define Etat1_2 2
#define Etat1_3 3
#define Etat1_4 4
#define Etat1_succes 5
#define Etat1_erreur 6

//Automate 2:
#define Etat2_debut 1
#define Etat2_2 2
#define Etat2_3 3
#define Etat2_4 4
#define Etat2_5 5
#define Etat2_succes 6
#define Etat2_erreur 7

void affiche_un_motif (char *str, int deb, int fin) {
	if (deb>fin)
	{
		printf("	");
		return;
	}
	printf("%c", str[deb]);
	affiche_un_motif (str, deb+1, fin);
}

void affiche_motifs(int *taboccur, int indocc, int nbocc, char *str)
{
	if (indocc >= nbocc*2)
	{
		printf("\n");
		return;
	}
	affiche_un_motif(str, taboccur[indocc], taboccur[indocc+1]);
	affiche_motifs(taboccur, indocc+2, nbocc, str);
}

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
	char tab_occ1[100][100];
	char tab_occ2[100][100];
	
	int ti = 0;
	
	int etat_actuel = 1;
	
	//tableau qui va stoker les lettres au fur et a mesure que on les valide
	char tab_verif[10] = {'X','X','X','X','X','X','X','X','X','X'};
	
	int a = 0;
	
	//Tableau stockant les indice de début et de fin
	int tab_indice1[100][2];
	int tab_indice2[100][2];
	
	int indice_debut = 0;
	int indice_fin = 0;
	
	//nombre d'occurence
	int nb_occ1 = 0;
	int nb_occ2 = 0;
//-------------------------------------------------------------------------------
	int i = 0;
// Automate 1 :

	while (i != x)
	{
		if ((etat_actuel == Etat1_debut) && (tab[i] == 'B'))
		{
			tab_verif[a] = 'B';
			indice_debut = i;
			a++;
		
			etat_actuel = Etat1_2;
		}
		else if ((etat_actuel == Etat1_2) && (tab[i] == 'B'))
		{
			tab_verif[a] = 'B';
			a++;
		}
		else if ((etat_actuel == Etat1_2) && (tab[i] == 'S'))
		{
			tab_verif[a] = 'S';
			a++;
			
			etat_actuel = Etat1_3;
		}
		else if ((etat_actuel == Etat1_3) && (tab[i] == 'Q'))
		{
			tab_verif[a] = 'Q';
			a++;
			
			etat_actuel = Etat1_4;
		}
		else if ((etat_actuel == Etat1_3) && (tab[i] == 'O'))
		{
			tab_verif[a] = 'O';
			
			etat_actuel = Etat1_succes;
		}
		else if ((etat_actuel == Etat1_4) && (tab[i] == 'Q'))
		{
			tab_verif[a] = 'Q';
			a++;
		}
		else if ((etat_actuel == Etat1_4) && (tab[i] == 'O'))
		{
			tab_verif[a] = 'O';
			etat_actuel = Etat1_succes;
		}
		else
		{
			etat_actuel = Etat1_erreur;
		}
	
		if (etat_actuel == Etat1_succes)
		{
			indice_fin = i;
			tab_indice1[ti][0] = indice_debut;
			tab_indice1[ti][1] = indice_fin;
			nb_occ1++;
			
			for(int j=0; j<=9; j++)
			{
				if(tab_verif[j] == 'B')
					strcat(tab_occ1[ti],"B");
								
				else if(tab_verif[j] == 'S')
					strcat(tab_occ1[ti],"S");
								
				else if(tab_verif[j] == 'Q')
					strcat(tab_occ1[ti],"Q");
								
				else if(tab_verif[j] == 'O')
					strcat(tab_occ1[ti],"O");
			}
			
			a = 0;
			indice_debut = 0;
			indice_fin = 0;
			ti++;
			etat_actuel = Etat1_debut;
			
			for(int j=0; j<10; j++)
			{ 
				 tab_verif[j] = 'X';
			}
		}
		else if (etat_actuel == Etat1_erreur)
		{
			a = 0;
			indice_debut = 0;
			indice_fin = 0;
			for(int j=0; j<10;j++)
			{ 
				 tab_verif[j] = 'X'; 
			}
			etat_actuel = Etat1_debut;
			//printf("Modèle non conforme\n");
		}
		i++;
	}
	
	printf("Motif 1 : B+SQ*O\n\n");
	printf("Affichage table des occurrences\n");
	
	for(int z = 0; z <= nb_occ1 -1; z++)
	{
		printf("%s", tab_occ1[z]);
		printf(" [%d  %d]\n", tab_indice1[z][0], tab_indice1[z][1]);
	}
	
	printf("%d motifs 1 trouvés\n\n", nb_occ1);
	
// Automate 2 :
	
	ti = 0;
	a = 0;
	etat_actuel = 1;
	
	for(int j=0; j<9;j++)
	{ 
		tab_verif[j] = 'X'; 
	}
	i=0;
	
	while (i != x)
	{
		if ((etat_actuel == Etat2_debut) && (tab[i] == 'B'))
		{
			tab_verif[a] = 'B';
			indice_debut = i;
			a++;
		
			etat_actuel = Etat2_2;
		}
		else if ((etat_actuel == Etat2_2) && (tab[i] == 'Q'))
		{
			tab_verif[a] = 'Q';
			a++;
			
			etat_actuel = Etat2_4;
		}
		else if ((etat_actuel == Etat2_2) && (tab[i] == 'S'))
		{
			tab_verif[a] = 'S';
			a++;
			
			etat_actuel = Etat2_3;
		}
		else if ((etat_actuel == Etat2_3) && (tab[i] == 'Q'))
		{
			tab_verif[a] = 'Q';
			a++;
			
			etat_actuel = Etat2_4;
		}
		else if ((etat_actuel == Etat2_4) && (tab[i] == 'O'))
		{
			tab_verif[a] = 'O';
			a++;
			
			etat_actuel = Etat2_5;
		}
		else if ((etat_actuel == Etat2_4) && (tab[i] != 'O'))
		{
			i--;
			etat_actuel = Etat2_succes;
		}
		else if ((etat_actuel == Etat2_5) && (tab[i] == 'O'))
		{
			tab_verif[a] = 'O';
		}
		else if ((etat_actuel == Etat2_5) && (tab[i] != 'O'))
		{
			i--;
			etat_actuel = Etat2_succes;
		}
		
		else
		{
			etat_actuel = Etat2_erreur;
		}
	
		if (etat_actuel == Etat2_succes)
		{
			indice_fin = i;
			tab_indice2[ti][0] = indice_debut;
			tab_indice2[ti][1] = indice_fin;
			nb_occ2++;
			
			for(int j=0; j<=9; j++)
			{
				if(tab_verif[j] == 'B')
					strcat(tab_occ2[ti],"B");
								
				else if(tab_verif[j] == 'S')
					strcat(tab_occ2[ti],"S");
								
				else if(tab_verif[j] == 'Q')
					strcat(tab_occ2[ti],"Q");
								
				else if(tab_verif[j] == 'O')
					strcat(tab_occ2[ti],"O");
			}
			
			a = 0;
			indice_debut = 0;
			indice_fin = 0;
			ti++;
			etat_actuel = Etat2_debut;
			
			for(int j=0; j<9; j++)
			{ 
				 tab_verif[j] = 'X';
			}
		}
		
		else if(etat_actuel == Etat2_erreur)
		{
			a = 0;
			indice_debut = 0;
			indice_fin = 0;
			for(int j=0; j<9;j++)
			{
				 tab_verif[j] = 'X';
			}
			etat_actuel = Etat2_debut;
			//printf("Modèle non conforme\n");
		}
		i++;
	}
	
	printf("Motif 2 : BS?QO*\n\n");
	printf("Affichage table des occurrences\n");
	
	for(int z = 0; z <= nb_occ2-1; z++)
	{
		printf("%s", tab_occ2[z]);
		printf(" [%d  %d]\n", tab_indice2[z][0], tab_indice2[z][1]);
	}
	
	printf("%d motifs 2 trouvés\n\n", nb_occ2);
	
// Utilisation des fonctions
	
	printf("affiche_motifs \n\n");
	
//motif 1 :
	
	printf("Motif 1 : B+SQ*O\n");
	
	affiche_motifs(tab_indice1, 0, nb_occ1, tab);
	printf("\n");
	affiche_un_motif(tab_occ1, 0, nb_occ1);
	printf("\n\n");
	
//motif 2 :
	
	printf("Motif 2 : BS?QO*\n");
	affiche_motifs(tab_indice2, 0, nb_occ2, tab);
	printf("\n");
	affiche_un_motif(tab_occ1, 0, nb_occ2);
	printf("\n");
}
