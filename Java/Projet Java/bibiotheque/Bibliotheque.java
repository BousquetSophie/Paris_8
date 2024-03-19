import java.util.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;


public class Bibliotheque
{
	public static void main(String[]args)
	{
		Livre livre=new Livre();
		Long ISBN=0L;
		Map<String, Livre> Dico = new HashMap<>();
		livre.setTitre("test");
		livre.setNomAuteur("testAuteur");
		livre.setPrenomAuteur("PrenomAuteur");
		livre.setCategorie("Roman");
		livre.setISBN(23452L);
		String s=livre.setCodeEnregistrement();//putain �a  retourne un string
		livre.CodeEnregistrement=s;
		System.out.println("livre par d�faut");

		System.out.println(livre.getCode());  //OK

		Dico.put(livre.getCode(), livre);
		Livre livre2=new Livre();
		livre2.setTitre("test2");
		livre2.setNomAuteur("testAuteur2");
		livre2.setPrenomAuteur("PrenomAuteur2");
		livre2.setCategorie("Roman");
		livre2.setISBN(23453L);
		s=livre2.setCodeEnregistrement();//putain �a  retourne un string
		livre2.CodeEnregistrement=s;
		System.out.println("livre par d�faut3");

		System.out.println(livre2.getCode());  //OK

		Dico.put(livre2.getCode(), livre2);

		
		
		
		ListeDeLivres listeDeLivres=new ListeDeLivres(Dico);
		    	 
		//InterfaceGraphique fenetre= new InterfaceGraphique (listeDeLivres);
		Fenetre App = new Fenetre(listeDeLivres);

	}
//	FileWriter MonFichier = new FileWriter("fichier.dat", true);
}
