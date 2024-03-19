import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;
import java.util.Set;

public class ListeDeLivres				//t'as pas besoin de besoin de faire extend
{ 
	protected Map<String, Livre> Dico = new HashMap<>();
	
	
	/* Cr�ation de la liste d'�l�ments de type "Type" et de type HashMap par d�faut */
	public ListeDeLivres(Map<String, Livre> Dico)
	{
		this.Dico=Dico;
	}
	//t'as oubli� de cr�er le constructeur du coup c'est normal  
	public ListeDeLivres()
	{
		
	}


	/* Cr�ation de la m�thode pour ajouter un livre � la liste */
	public void ajouterLivre(Livre Bouquin)
	{
		this.Dico.putIfAbsent(Bouquin.getCode(), Bouquin);
	}//mets en r�f�rence la classe avec le this
	
	/* Cr�ation de la m�thode pour supprimer un livre de la liste */
	public void supprimerLivre()
	{
		System.out.println("Quelle est la cl� du livre ?");
		Scanner scan = new Scanner(System.in);
		String Cle = scan.next();
		
		Iterator<Map.Entry<String, Livre>> iter = this.Dico.entrySet().iterator();
		
		while(iter.hasNext())
		{
			Map.Entry<String, Livre> entr = iter.next();
			if (iter.next().getValue().getCode().equals(Cle))
			{
				iter.remove();											//Supprimer le livre qui a pour cl� d'assiciation "Bouquin.getCode()"
				break;
			}
		}								
	}
	
	/* Cr�ation de la m�thode pour rechercher un livre dans la liste */
	public void rechercherLivre()
	{
		System.out.println("Quelle est la cl� du livre ?");
		Scanner scan = new Scanner(System.in);
		String Cle = scan.next();
		
		Iterator<Map.Entry<String, Livre>> iter = this.Dico.entrySet().iterator();		
		while(iter.hasNext())
		{
			Map.Entry<String, Livre> entr = iter.next();
			if (iter.next().getValue().getCode().equals(Cle))
			{
				System.out.println("Le livre existe !");
				iter.next().getValue().afficheLivre();
				break;
			}
		} 
	}
	
	public void afficherLesLivres()
	{
		Iterator<Map.Entry<String, Livre>> iter = this.Dico.entrySet().iterator();
		System.out.println("Liste des livres enregistr�s :");
		while(iter.hasNext())
		{
			Map.Entry<String, Livre> entr = iter.next();
			System.out.println("\t" +entr.getKey() +":" +entr.getValue().getTitre());
		}
	}
	
}
