#include <iostream>
#include <vector>
#include <random>
#include <time.h>

using namespace std;

// initialisation des lettres a utiliser
#define CHAR_MOUTON ('M')
#define CHAR_LOUP ('L')
#define CHAR_SELL ('S')
#define CHAR_NO_HERBE ('/')
#define CHAR_HERBE (' ')

class eco_plateau
{
	public :
		
		char plateau[9][9];
		
		eco_plateau() {};
		
		void init_plateau()
		{
			char lettre_plateau[8] = {'A','B','C','D','E','F','G','H'};
			//char chiffre_plateau[8] = {'1','2','3','4','5','6','7','8'};
			
			plateau[0][0] = ' ';
			
			//mettre lettre dans tableau
			for(int i = 0; i <= 8; i++)
			{
				plateau[0][i+1] = lettre_plateau[i];
			}
			
			//mettre chiffre dans tableau
			plateau[1][0] = '1';
			plateau[2][0] = '2';
			plateau[3][0] = '3';
			plateau[4][0] = '4';
			plateau[5][0] = '5';
			plateau[6][0] = '6';
			plateau[7][0] = '7';
			plateau[8][0] = '8';
			
			//remplir case vide
			for(int i = 1; i <= 8; i++)
			{
				for(int j = 1; j <= 8; j++)
				{
					plateau[i][j] = ' ';
				}
			}
		}
		
		void affiche_plateau()
		{
			// afficher lettre
			for(int j = 0; j <= 8; j++)
			{
				cout << " " << plateau[0][j]<< " "<< " ";
			}
			cout << endl;
			cout << "   " << "+---+---+---+---+---+---+---+---+" <<endl;
			
			// afficher tableau
			for(int i = 1; i <= 8; i++)
			{
				for(int j = 0; j <= 8; j++)
				{
					cout <<" "<< plateau[i][j]<<" "<< "|";
				}
				cout << endl;
				cout << "   " << "+---+---+---+---+---+---+---+---+" <<endl;
			}
			cout << endl;
		}
		
		//ajoute/supprime/modifie des lettres dans le plateau
		void modifier_lettre(char lettre, int l, int c)
		{
			plateau[l][c] = lettre;
		}
};

class Animal
{
    int ligne;
	int colonne;
	char sexe;
	
    int age = 0; //50 tour avant mort
    int jour_manger = 0; //5 jour sans manger, meurt au 6eme

    public :

    	Animal(int ligne, int colone,char sexe)
    	{
        	this->ligne = ligne;
        	this->colonne = colone;
        	this->sexe = sexe;
    	}

    	// get et set
    	int get_ligne()
    	{
        	//cout << l << endl;
        	return this->ligne;
    	}
    	int get_colone()
    	{
        	//cout << c << endl;
        	return this->colonne;
    	}
    	char get_sexe()
    	{
        	return this->sexe;
    	}
    
    	void set_ligne(int ligne)
    	{
        	this->ligne = ligne;
    	}
    	void set_colone(int colone)
    	{
        	this->colonne = colone;
    	}
};

class Mouton : public Animal
{

	public :

		static int nb_mouton;
		int jour_manger = 0;
		int age = 0;
		char anterieur_pos_lettre = ' '; //stock la valeur qu'il y avait avant qu'il aille sur la case
    
		Mouton(int ligne, int colonne,char sexe) : Animal(ligne, colonne, sexe)
		{
			nb_mouton++;
		}
		~Mouton() {nb_mouton--;};
		
		int get_nbmouton()
		{
			return nb_mouton;
		}
		
		int verif_mort()
		{
			if(jour_manger == 6) //déplacer les constantes
				return 1;
				
			else if(age == 50)
				return 1;
			
			else 
				return 0;
		}	
};

class loup : public Animal
{
	public :
		static int nb_loup;
		int jour_manger = 0;
		int age = 0;
		char anterieur_pos_lettre = ' ';//stock la valeur qu'il y avait avant qu'il aille sur la case
		
		loup(int ligne, int colonne, char sexe) : Animal(ligne, colonne, sexe)
		{

			nb_loup++;
		}
		~loup() {nb_loup--;};
		
		int get_nbloup()
		{
			return nb_loup;
		}
		
		int verif_mort()
		{
			if(jour_manger == 11)
				return 1;
				
			else if(age == 61)
				return 1;
			
			else 
				return 0;
		}
};

vector<int> alea_pos(eco_plateau a) 
{
	int ligne = 0;
	int colone = 0;
	
	while(true)
	{
		//valeur aléatoire
		srand(time(NULL));
		ligne = rand()%8 + 1;
		colone = rand()%8 + 1;
		
		if(a.plateau[ligne][colone] == ' ')
		{
			break;
		}
	}
	
	
	vector<int> pos;
	pos.push_back(ligne);
	pos.push_back(colone);
	
	return pos;
}

vector<int> deplacement(int pos_l, int pos_c, eco_plateau a)
{
	int tab_index[9][2];
	int new_l = 0;
	int new_c = 0;
	int i = 0;
	
	//ne bouge pas
	tab_index[i][0]  = pos_l;
	tab_index[i][1]  = pos_c;
	i++;
	
	//haut
	if(((pos_l-1 > 0) && (pos_c > 0)) && ((pos_l-1 < 9) && (pos_c < 9)))//bordure
	{
		if((a.plateau[pos_l-1][pos_c] != 'M') || (a.plateau[pos_l-1][pos_c] != 'L'))
		{
			tab_index[i][0]  = pos_l-1;
			tab_index[i][1]  = pos_c;
			i++;
		}
		
	}
	
	//bas
	if(((pos_l+1 > 0) && (pos_c > 0)) && ((pos_l+1 < 9) && (pos_c < 9)))//bordure
	{
		if((a.plateau[pos_l+1][pos_c] != 'M') || (a.plateau[pos_l+1][pos_c] != 'L'))
		{
			tab_index[i][0]  = pos_l+1;
			tab_index[i][1]  = pos_c;
			i++;
		}
	}
	
	//gauche
	if(((pos_l > 0) && (pos_c-1 > 0)) && ((pos_l < 9) && (pos_c-1 < 9)))//bordure
	{
		if((a.plateau[pos_l][pos_c-1] != 'M') || (a.plateau[pos_l][pos_c-1] != 'L'))
		{
			tab_index[i][0]  = pos_l;
			tab_index[i][1]  = pos_c-1;
			i++;
		}
	}
	
	//droite
	if(((pos_l > 0) && (pos_c+1 > 0)) && ((pos_l < 9) && (pos_c+1 < 9)))//bordure
	{
		if((a.plateau[pos_l][pos_c+1] != 'M') || (a.plateau[pos_l][pos_c+1] != 'L'))
		{
			tab_index[i][0]  = pos_l;
			tab_index[i][1]  = pos_c+1;
			i++;
		}
	}
	
	//haut gauche
	if(((pos_l-1 > 0) && (pos_c-1 > 0)) && ((pos_l-1 < 9) && (pos_c-1 < 9)))//bordure
	{
		if((a.plateau[pos_l-1][pos_c-1] != 'M') || (a.plateau[pos_l-1][pos_c-1] != 'L'))
		{
			tab_index[i][0]  = pos_l-1;
			tab_index[i][1]  = pos_c-1;
			i++;
		}
	}
	
	//haut droite
	if(((pos_l-1 > 0) && (pos_c+1 > 0)) && ((pos_l-1) < 9 && (pos_c+1 < 9)))//bordure
	{
		if((a.plateau[pos_l-1][pos_c+1] != 'M') || (a.plateau[pos_l-1][pos_c+1] != 'L'))
		{
			tab_index[i][0]  = pos_l-1;
			tab_index[i][1]  = pos_c+1;
			i++;
		}
	}
	
	//bas gauche
	if(((pos_l+1 > 0) && (pos_c-1 > 0)) && ((pos_l+1 < 9) && (pos_c-1 < 9)))//bordure
	{
		if((a.plateau[pos_l+1][pos_c-1] != 'M') || (a.plateau[pos_l+1][pos_c-1] != 'L'))
		{
			tab_index[i][0]  = pos_l+1;
			tab_index[i][1]  = pos_c-1;
			i++;
		}
	}
	
	//bas droite
	if(((pos_l+1 > 0) && (pos_c+1 > 0)) && ((pos_l+1 < 9) && (pos_c+1 < 9)))//bordure
	{
		if((a.plateau[pos_l+1][pos_c+1] != 'M') || (a.plateau[pos_l+1][pos_c+1] != 'L'))
		{
			tab_index[i][0]  = pos_l+1;
			tab_index[i][1]  = pos_c+1;
			i++;
		}
	}
	
	srand(time(NULL));
	int alea = 0;
	alea = rand()%i + 0;
	
	new_l = tab_index[alea][0];
	new_c = tab_index[alea][1];
	
	vector<int> lst;
	lst.push_back(new_l);
	lst.push_back(new_c);
	
	/*for(int i = 0; i <= nb_valeur; i++)
		cout<<tab_index[i][0]<< " " << tab_index[i][1]<<endl;
	cout<<endl;*/
	return lst;
}

void mouton_manger(Mouton* m)
{
	if(m->anterieur_pos_lettre == ' ')
		m->jour_manger = 0;
	else
		m->jour_manger++;
}

vector<int> loup_manger(loup* l, eco_plateau a)
{
	vector<int> mouton;
	int pos_l = l->get_ligne();
	int pos_c = l->get_colone();
	
	//haut
	if(a.plateau[pos_l-1][pos_c] == 'M')
	{
		l->jour_manger = 0;
		mouton.push_back(pos_l-1);
		mouton.push_back(pos_c);
	}
	
	//bas
	else if(a.plateau[pos_l+1][pos_c] == 'M')
	{
		l->jour_manger = 0;
		mouton.push_back(pos_l+1);
		mouton.push_back(pos_c);
	}
	
	//gauche
	else if(a.plateau[pos_l][pos_c-1] == 'M')
	{
		l->jour_manger = 0;
		mouton.push_back(pos_l);
		mouton.push_back(pos_c-1);
	}
	
	//droite
	else if(a.plateau[pos_l][pos_c+1] == 'M')
	{
		l->jour_manger = 0;
		mouton.push_back(pos_l);
		mouton.push_back(pos_c+1);
	}
	
	//haut gauche
	else if(a.plateau[pos_l-1][pos_c-1] == 'M')
	{
		l->jour_manger = 0;
		mouton.push_back(pos_l-1);
		mouton.push_back(pos_c-1);
	}
	
	//haut droite
	else if(a.plateau[pos_l-1][pos_c+1] == 'M')
	{
		l->jour_manger = 0;
		mouton.push_back(pos_l-1);
		mouton.push_back(pos_c+1);
	}
	
	//bas gauche
	else if(a.plateau[pos_l+1][pos_c-1] == 'M')
	{
		l->jour_manger = 0;
		mouton.push_back(pos_l+1);
		mouton.push_back(pos_c-1);
	}
	
	//bas droite
	else if(a.plateau[pos_l+1][pos_c+1] == 'M')
	{
		l->jour_manger = 0;
		mouton.push_back(pos_l+1);
		mouton.push_back(pos_c+1);
	}
	
	else
	{
		l->jour_manger++;
		mouton.push_back(10);
	}
	return mouton;
}

int verif_mouton(Mouton* m, int l, int c)
{
	if((m->get_ligne() == l) && (m->get_colone() == c))
			return 0;
	else
		return 1;
}

//int naissance_mouton() (0 ok, 1 non)
//int naissance_loup()  (0 ok, 1 non)

int Mouton::nb_mouton = 0;
int loup::nb_loup = 0;

int main()
{
	//index pour les déplacement
	vector<int> mouvement;
	
	//index pour les positions aleatoire
	vector<int> pos;
	
	// initialisation des tours
	int tours = 1;
	
	// position du mouton que le loup va manger
	vector<int> loupManger;
	
	// liste de stocage des sels
	int lst_sels[64][3]; //ligne, colone, tours
	int s = 0;//initialisation
	int s1 = 0;//tour d'avant
	
	//création et initialisation du plateau
	eco_plateau plt_principal{};
	plt_principal.init_plateau();

	//on utilise new pour pouvoir delete l'objet lors de la mort
	//initialisation des moutons de base
	pos = alea_pos(plt_principal);
	Mouton* mouton1 = new Mouton(pos[0],pos[1],'F');
	plt_principal.modifier_lettre(CHAR_MOUTON, mouton1->get_ligne(), mouton1->get_colone());
	pos.clear();
	
	pos = alea_pos(plt_principal);
	Mouton* mouton2 = new Mouton(pos[0],pos[1],'M');
	plt_principal.modifier_lettre(CHAR_MOUTON, mouton2->get_ligne(), mouton2->get_colone());
	pos.clear();
	
	pos = alea_pos(plt_principal);
	Mouton* mouton3 = new Mouton(pos[0],pos[1],'F');
	plt_principal.modifier_lettre(CHAR_MOUTON, mouton3->get_ligne(), mouton3->get_colone());
	pos.clear();
	
	//initialisation des loups de base
	pos = alea_pos(plt_principal);
	loup* loup1 = new loup(pos[0],pos[1],'F');
	plt_principal.modifier_lettre(CHAR_LOUP, loup1->get_ligne(), loup1->get_colone());
	pos.clear();
	
	pos = alea_pos(plt_principal);
	loup* loup2 = new loup(pos[0],pos[1],'M');
	plt_principal.modifier_lettre(CHAR_LOUP, loup2->get_ligne(), loup2->get_colone());
	pos.clear();
	
	//Affiche le plateau initiale
	plt_principal.affiche_plateau();
	cout << "Tours : " << tours << " | Loups : " << loup::nb_loup << " | Moutons : " << Mouton::nb_mouton <<endl;
	cout<<endl;
	
	while(true)
	{
		for(int i = 0; i < s1; i++)
		{
			if(lst_sels[i][2] == tours)
				plt_principal.modifier_lettre(CHAR_HERBE,lst_sels[i][0],lst_sels[i][1]);
		}
		s1 = s;
		s = 0;
		
		if(mouton1 != nullptr)
		{
			if(mouton1->verif_mort())
			{
				if(mouton1->anterieur_pos_lettre == '/')
				{
					plt_principal.modifier_lettre(CHAR_SELL, mouton1->get_ligne(), mouton1->get_colone());
					lst_sels[s][0]= mouton1->get_ligne();
					lst_sels[s][1]= mouton1->get_colone();
					lst_sels[s][2]= tours+=2; //tour initialiser et tour suivant
					s++;
				}
				plt_principal.modifier_lettre(CHAR_HERBE, mouton1->get_ligne(), mouton1->get_colone());
				delete mouton1;
				mouton1 = nullptr;
			}
		}
		
		if(mouton1 != nullptr)//reverifie si le mouton est toujours en vie pour eviter les erreurs
		{
			mouton_manger(mouton1);
			mouvement = deplacement(mouton1->get_ligne(),mouton1->get_colone(), plt_principal);
			plt_principal.modifier_lettre(CHAR_NO_HERBE, mouton1->get_ligne(), mouton1->get_colone());
			mouton1->anterieur_pos_lettre = plt_principal.plateau[mouvement[0]][mouvement[1]];
			mouton1->set_ligne(mouvement[0]);
			mouton1->set_colone(mouvement[1]);
			plt_principal.modifier_lettre(CHAR_MOUTON, mouton1->get_ligne(), mouton1->get_colone());
			mouvement.clear();
			//cout << "M1"<<endl;
			//plt_principal.affiche_plateau();
			mouton1->age++;
		}
		
		if(mouton2 != nullptr)
		{
			if(mouton2->verif_mort())
			{
				if(mouton2->anterieur_pos_lettre == '/')
				{
					plt_principal.modifier_lettre(CHAR_SELL, mouton2->get_ligne(), mouton2->get_colone());
					lst_sels[s][0]= mouton2->get_ligne();
					lst_sels[s][1]= mouton2->get_colone();
					lst_sels[s][2]= tours+=2; //tour initialiser et tour suivant
					s++;
				}
				plt_principal.modifier_lettre(CHAR_HERBE, mouton2->get_ligne(), mouton2->get_colone());
				delete mouton2;
				mouton2 = nullptr;
			}
		}
		
		if(mouton2 != nullptr)//reverifie si le mouton est toujours en vie pour eviter les erreurs
		{
			mouton_manger(mouton2);
			mouvement = deplacement(mouton2->get_ligne(),mouton2->get_colone(), plt_principal);
			plt_principal.modifier_lettre(CHAR_NO_HERBE, mouton2->get_ligne(), mouton2->get_colone());
			mouton2->anterieur_pos_lettre = plt_principal.plateau[mouvement[0]][mouvement[1]];
			mouton2->set_ligne(mouvement[0]);
			mouton2->set_colone(mouvement[1]);
			plt_principal.modifier_lettre(CHAR_MOUTON, mouton2->get_ligne(), mouton2->get_colone());
			mouvement.clear();
			//cout << "M2"<<endl;
			//plt_principal.affiche_plateau();
			mouton2->age++;
		}
		
		if(mouton3 != nullptr)
		{
			if(mouton3->verif_mort())
			{
				if(mouton3->anterieur_pos_lettre == '/')
				{
					plt_principal.modifier_lettre(CHAR_SELL, mouton3->get_ligne(), mouton3->get_colone());
					lst_sels[s][0]= mouton3->get_ligne();
					lst_sels[s][1]= mouton3->get_colone();
					lst_sels[s][2]= tours+=2; //tour initialiser et tour suivant
					s++;
				}
				plt_principal.modifier_lettre(CHAR_HERBE, mouton3->get_ligne(), mouton3->get_colone());
				delete mouton3;
				mouton3 = nullptr;
			}
		}
		
		if(mouton3 != nullptr)//reverifie si le mouton est toujours en vie pour eviter les erreurs
		{
			mouton_manger(mouton3);
			mouvement = deplacement(mouton3->get_ligne(),mouton3->get_colone(), plt_principal);
			plt_principal.modifier_lettre(CHAR_NO_HERBE, mouton3->get_ligne(), mouton3->get_colone());
			mouton3->anterieur_pos_lettre = plt_principal.plateau[mouvement[0]][mouvement[1]];
			mouton3->set_ligne(mouvement[0]);
			mouton3->set_colone(mouvement[1]);
			plt_principal.modifier_lettre(CHAR_MOUTON, mouton3->get_ligne(), mouton3->get_colone());
			mouvement.clear();
			//cout << "M3"<<endl;
			//plt_principal.affiche_plateau();
			mouton3->age++;
		}
		
		if(loup1 != nullptr)
		{
			if(loup1->verif_mort())
			{
				if(loup1->anterieur_pos_lettre == '/')
				{
					plt_principal.modifier_lettre(CHAR_SELL, loup1->get_ligne(), loup1->get_colone());
					lst_sels[s][0]= loup1->get_ligne();
					lst_sels[s][1]= loup1->get_colone();
					lst_sels[s][2]= tours+=2; //tour initialiser et tour suivant
					s++;
				}
				plt_principal.modifier_lettre(CHAR_HERBE, loup1->get_ligne(), loup1->get_colone());
				delete loup1;
				loup1 = nullptr;
			}
		}
		
		if(loup1 != nullptr)//reverifie si le loup est toujours en vie pour eviter les erreurs
		{
			loupManger = loup_manger(loup1, plt_principal);
			if(loupManger[0] != 10)
			{
				if((mouton1 != nullptr)&&(verif_mouton(mouton1, loupManger[0], loupManger[1]) == 0))
				{
					plt_principal.modifier_lettre(mouton1->anterieur_pos_lettre, mouton1->get_ligne(), mouton1->get_colone());
					delete mouton1;
					mouton1 = nullptr;
				}
				else if((mouton2 != nullptr)&&(verif_mouton(mouton2, loupManger[0], loupManger[1]) == 0))
				{
					plt_principal.modifier_lettre(mouton2->anterieur_pos_lettre, mouton2->get_ligne(), mouton2->get_colone());
					delete mouton2;
					mouton2 = nullptr;
				}
				else if((mouton3 != nullptr)&&(verif_mouton(mouton3, loupManger[0], loupManger[1]) == 0))
				{
					plt_principal.modifier_lettre(mouton3->anterieur_pos_lettre, mouton3->get_ligne(), mouton3->get_colone());
					delete mouton3;
					mouton3 = nullptr;
				}
			}
		
			mouvement = deplacement(loup1->get_ligne(),loup1->get_colone(), plt_principal);
			plt_principal.modifier_lettre(loup1->anterieur_pos_lettre, loup1->get_ligne(), loup1->get_colone());
			loup1->anterieur_pos_lettre = plt_principal.plateau[mouvement[0]][mouvement[1]];
			loup1->set_ligne(mouvement[0]);
			loup1->set_colone(mouvement[1]);
			plt_principal.modifier_lettre(CHAR_LOUP, loup1->get_ligne(), loup1->get_colone());
			mouvement.clear();
			loupManger.clear();
			//cout << "L1"<<endl;
			//plt_principal.affiche_plateau();
			loup1->age++;
		}
		
		if(loup2 != nullptr)
		{
			if(loup2->verif_mort())
			{
				if(loup2->anterieur_pos_lettre == '/')
				{
					plt_principal.modifier_lettre(CHAR_SELL, loup2->get_ligne(), loup2->get_colone());
					lst_sels[s][0]= loup2->get_ligne();
					lst_sels[s][1]= loup2->get_colone();
					lst_sels[s][2]= tours+=2; //tour initialiser et tour suivant
					s++;
				}
				plt_principal.modifier_lettre(CHAR_HERBE, loup2->get_ligne(), loup2->get_colone());
				delete loup2;
				loup2 = nullptr;
			}
		}
		
		if(loup2 != nullptr)//reverifie si le loup est toujours en vie pour eviter les erreurs
		{
			loupManger = loup_manger(loup2, plt_principal);
			if(loupManger[0] != 10)
			{
				if((mouton1 != nullptr)&&(verif_mouton(mouton1, loupManger[0], loupManger[1]) == 0))
				{
					plt_principal.modifier_lettre(mouton1->anterieur_pos_lettre, mouton1->get_ligne(), mouton1->get_colone());
					delete mouton1;
					mouton1 = nullptr;
				}
				else if((mouton2 != nullptr)&&(verif_mouton(mouton2, loupManger[0], loupManger[1]) == 0))
				{
					plt_principal.modifier_lettre(mouton2->anterieur_pos_lettre, mouton2->get_ligne(), mouton2->get_colone());
					delete mouton2;
					mouton2 = nullptr;
				}
				else if((mouton3 != nullptr)&&(verif_mouton(mouton3, loupManger[0], loupManger[1]) == 0))
				{
					plt_principal.modifier_lettre(mouton3->anterieur_pos_lettre, mouton3->get_ligne(), mouton3->get_colone());
					delete mouton3;
					mouton3 = nullptr;
				}
			}
			mouvement = deplacement(loup2->get_ligne(),loup2->get_colone(), plt_principal);
			plt_principal.modifier_lettre(loup2->anterieur_pos_lettre, loup2->get_ligne(), loup2->get_colone());
			loup2->anterieur_pos_lettre = plt_principal.plateau[mouvement[0]][mouvement[1]];
			loup2->set_ligne(mouvement[0]);
			loup2->set_colone(mouvement[1]);
			plt_principal.modifier_lettre(CHAR_LOUP, loup2->get_ligne(), loup2->get_colone());
			mouvement.clear();
			loupManger.clear();
			//cout << "L2"<<endl;
			//plt_principal.affiche_plateau();
			loup2->age++;
		}
	
		plt_principal.affiche_plateau();
		cout << "Tours : " << tours << " | Loups : " << loup::nb_loup << " | Moutons : " << Mouton::nb_mouton <<endl;
		cout<<endl;
		
		if((Mouton::nb_mouton == 0)&&(loup::nb_loup == 0))
		{
			cout<< "Il n'y a plus de mouton ni de loup en vie !"<<endl;
			cout<< "La partie est terminer !"<<endl;
			break;
		}
		
		tours++;
		
		char continuer;
		
		cout << "Voulez-vous passez au prochain tour ?(O/N)"<<endl;
		cin >> continuer;
		cout << endl;
		
		if(continuer != 'O')
		{
			cout<< "La partie est terminer !"<<endl;
			break;
		}
	}
}
