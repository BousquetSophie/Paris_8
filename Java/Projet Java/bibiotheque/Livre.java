public class Livre
{
	protected long ISBN;
	protected String Titre, NomAuteur, PrenomAuteur, Categorie, CodeEnregistrement;
	//protected Livre Bouquin;
	
/* Constructeur par d�faut */
	public Livre()
	{
		this.Titre=null;
		this.NomAuteur=null;
		this.PrenomAuteur=null;
		this.Categorie=null;
		this.ISBN=0L;
		this.CodeEnregistrement=null;
	}
	
/* Constructeur exhaustif */
	public Livre(String Titre, String NomAuteur, String PrenomAuteur, String Categorie, int ISBN, String CodeEnregistrement)
	{
		this.Titre=Titre;
		this.NomAuteur=NomAuteur;
		this.PrenomAuteur=PrenomAuteur;
		this.Categorie=Categorie;
		this.ISBN=ISBN;
		this.CodeEnregistrement=null;
	}
	
/* Liste de set et de get */
	public void setISBN(long ISBN)
	{
		this.ISBN=ISBN;
	}
	public long getISBN()
	{
		return ISBN;
	}
	
	public void setCode(String Code)
	{
		this.CodeEnregistrement=Code;
	}
	public String getCode()
	{
		return CodeEnregistrement;
	}
	
	public void setTitre(String Titre)
	{
		this.Titre=Titre;
	}
	public String getTitre()
	{
		return Titre;
	}
	
	public void setPrenomAuteur(String PreAut)
	{
		this.PrenomAuteur=PreAut;
	}
	public String getPrenomAuteur()
	{
		return PrenomAuteur;
	}
	
	public void setNomAuteur(String NomAut)
	{
		this.NomAuteur=NomAut;
	}
	public String getNomAuteur()
	{
		return NomAuteur;
	}
	
	public void setCategorie(String Categorie)
	{
		this.Categorie=Categorie;
	}
	public String getCategorie()
	{
		return Categorie;
	}

/* Cr�ation de la m�thode affiche*/
	public void afficheLivre()
	{
		System.out.println("Livre enregistr� :\nTitre du livre: " +Titre +"\nCode d'enregistrement : " +CodeEnregistrement);
	}
	
/* Fonction pour calculer le code d'enregistrement */
	
	public String setCodeEnregistrement()
	{	
		/* Isolement des lettres des nom et pr�nom de l'auteur */
		char LettreNom1 = NomAuteur.charAt(0);
		char LettreNom2 = NomAuteur.charAt(1);
		char LettrePrenom1 = PrenomAuteur.charAt(0);
		char LettrePrenom2 = PrenomAuteur.charAt(1);
		
		/* Cr�ation de l'indice de la cat�gorie */
		String Cat = null;
		
		switch(Categorie)
		{
			case("Junior"):
			{
				Cat = "Ju";
				break;
			}
			case("Philosophie"):
			{
				Cat = "Ph";
				break;
			}
			case("Policier"):
			{
				Cat = "Po";
				break;
			}
			case("Roman"):
			{
				Cat = "Ro";
				break;
			}
			case("Sciencefiction"):
			{
				Cat = "Sf";
				break;
			}
			default:
			{
				System.out.println("Not a book category");
			}
		}				
		
		/* Isolement des deux derniers chiffres du code ISBN */
		ISBN-=(ISBN/100)*100;

		/*Concat�nation des diff�rents �l�ments */
		String LettresNom = new StringBuilder().append(LettreNom1).append(LettreNom2).toString();
		String LettresPrenom = new StringBuilder().append(LettrePrenom1).append(LettrePrenom2).toString();
		String CodeEnregistrement = LettresNom +LettresPrenom +Cat +ISBN;
		
		/* On envoie le code d'enregistrement */
		return CodeEnregistrement;
	}
}
