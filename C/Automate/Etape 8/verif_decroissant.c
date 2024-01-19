#include <stdio.h>
#include <string.h>
#include <assert.h>

int main()
{	
	int nb_occ1 = 7;
	int nb_occ2 = 9;
	
	char automate1[100][100] = {"BSQO","BBSQO","BQO","BSQOO","BSO","BSQQO"};
	char automate2[100][100] = {"BSQO","BSQO","BBBSQO","BQO","BSOO","BSO","BSSQQO","BSO","BSO"};
	
// Union des 2 Automate :

	char union_auto[1000][1000];
	int occurence[100];
	int e = 0;
	int nb_motif = 0;
	int verif_doublon = 0;
	
	for(int i = 0; i < nb_occ1; i++)
	{
		for(int j = 0; j < nb_occ2; j++)
		{
			if(strcmp(automate1[i], automate2[j]) == 0)
			{
				for(int k = 0; k < 10; k++)
				{
					if(strcmp(automate1[i], union_auto[k]) == 0)
					{
						verif_doublon++;
						occurence[k]++;
					}
				}
				
				if(verif_doublon == 0)
				{
					strcat(union_auto[e],automate1[i]);
					nb_motif ++;
					occurence[e] = 1;
					e++;
				}
				verif_doublon = 0;
			}
		}
	}
	
// Classer par ordre décroisant

	int occ_tries[nb_motif];
	char union_tries[1000][1000];
	int max = 0;
	
	for(int i = 0; i < nb_motif; i++)
	{
		for(int indice = 0; indice < nb_motif; indice++)
		{
			if(occurence[max] <= occurence[indice])
			{
				max = indice;
			}
		}
		
		occ_tries[i] = occurence[max];
		strcat(union_tries[i],union_auto[max]);
		occurence[max] = 0;
		max = 0;
	}
	
	printf("Union par ordre décroissant des motifs obtenu\n");
	
	for(int i = 0; i < nb_motif; i++)
	{
		printf("%s %d \n", union_tries[i], occ_tries[i]);
	}

// Vérification des Union par ordre décroissant

	char union_decroissant_ob[1000][1000] = {"BSO","BSQO","BQO"};
	int occurence_decroissant_ob[3] = {3,2,1};
	int nbmotif_ob = 3;
	
	printf("\n");
	printf("Union par ordre décroissant des motifs à obtenir\n");
	
	assert(nb_motif == nbmotif_ob);
	
	for(int i = 0; i < nbmotif_ob; i++)
	{
		printf("%s %d\n", union_decroissant_ob[i], occurence_decroissant_ob[i]);
	}
	
	for(int i = 0; i < nbmotif_ob; i++)
	{
		assert(strcmp(union_decroissant_ob[i], union_tries[i]) == 0);
		assert(occ_tries[i] == occurence_decroissant_ob[i]);
	}
}
