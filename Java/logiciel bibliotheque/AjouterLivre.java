import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Scanner;

public class AjouterLivre implements ActionListener {

	protected ListeDeLivres listeDelivres;
	protected AjouterLivre(ListeDeLivres listeDelivres) {
		this.listeDelivres=listeDelivres;
	}

	public void actionPerformed(ActionEvent e)
	{

		// Bloc lecture au clavier des coordonn�es du livre

		
		/* M�thode avec le constructeur par d�faut */

		Livre Bouquin = new Livre();
		Long ISBN=0L;

		try ( Scanner scan = new Scanner( System.in ) ) {

			while(true ) {


				System.out.println("Entrez les donn�es du livre\nTitre");
				String Titre = scan.nextLine();
				System.out.println("Nom(Auteur)");
				String NomAuteur = scan.nextLine();

				System.out.println("Prenom (Auteur)");
				String PrenomAuteur = scan.nextLine();

				System.out.println("Cat�gorie (Roman, Science-fiction, Philosophie, Junior, Policier)");
				String Categorie = scan.nextLine();

				System.out.println("Num�ro ISBN");
				do
				{
					System.out.println("Code de 5(10) � 8(13) chifffres.");
					ISBN=Long.parseLong(scan.nextLine());
				}
				while(ISBN<(10000L) || ISBN>(10000000L));
				Bouquin.setTitre(Titre);
				Bouquin.setNomAuteur(NomAuteur);
				Bouquin.setPrenomAuteur(PrenomAuteur);
				Bouquin.setCategorie(Categorie);
				Bouquin.setISBN(ISBN);
				String s=Bouquin.setCodeEnregistrement();//putain �a  retourne un string
				Bouquin.CodeEnregistrement=s;

				System.out.println(Bouquin.getCode());  //OK

				this.listeDelivres.Dico.put(Bouquin.getCode(), Bouquin);

				System.out.println("continuer d'afficher:O/N");
				String Suite = scan.nextLine();
				if ( Suite.equals( "N" ) ) {
					scan.close();
					break;
				}
			}
		}
				
	}

}
