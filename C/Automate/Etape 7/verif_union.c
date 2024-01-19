#include <stdio.h>
#include <string.h>
#include <assert.h>

int main()
{	
	int nb_occ1 = 7;
	int nb_occ2 = 8;
	
	char automate1[100][100] = {"BSQO","BBSQO","BQO","BSQOO","BSO","BSQQO"};
	char automate2[100][100] = {"BSQO","BSQO","BBBSQO","BQO","BSOO","BSO","BSSQQO","BSO"};
	
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
	
	printf("Union des motifs obtenu\n");
	
	for(int i = 0; i < e; i++)
	{
		printf("%s %d \n", union_auto[i], occurence[i]);
	}
	
	printf("\n");
	
	printf("--> %d motifs uniques obtenu\n\n", nb_motif);
	
// Vérification des Union
	
	int nbmotif_ob = 3;
	char union_ob[1000][1000] = {"BSQO","BQO","BSO"};
	int occurence_ob[3] = {2,1,2};
	
	printf("Union des motifs à obtenir\n");
	
	for(int i = 0; i < nbmotif_ob; i++)
	{
		printf("%s %d\n", union_ob[i], occurence_ob[i]);
	}
	printf("\n");
	printf("--> %d motifs uniques à obtenir\n", nbmotif_ob);
	
	assert(nbmotif_ob == nb_motif);
	
	for(int i = 0; i < nbmotif_ob; i++)
	{
		assert(strcmp(union_ob[i], union_auto[i]) == 0);
		assert(occurence[i] == occurence_ob[i]);
	}
}
