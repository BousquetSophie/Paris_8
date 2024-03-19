import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;

import javax.swing.*;

public class Fenetre extends JFrame
{
	
	private static final long serialVersionUID = -5782047501280077401L;
	protected ListeDeLivres listeDelivres;
	public static JTextField textField=new JTextField();
	public Fenetre(ListeDeLivres listeDelivres)
	{
		this.listeDelivres=listeDelivres;
	    this.setTitle("Application Biblioth�que");					//Nom de la fen�tre
	    this.setSize(500, 500);
	    //Dimensions en pixel
	    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);		//Fermer la fen�tre en cliquant sur la croix rouge
	    this.setLocationRelativeTo(null);							//Placer la fen�tre au centre de l'�cran
	    JPanel panel = new JPanel();
	    setContentPane(panel);
	    panel.setSize(500,500);
	  
		textField.setColumns(10); //On lui donne un nombre de colonnes � afficher
 
		panel.add(textField);
	    JButton Bouton1 = new JButton("Afficher le livre");
	    	Bouton1.addActionListener(new AfficherLivre(listeDelivres));
	    	panel.add(Bouton1, BorderLayout.WEST);
	    	
	    JButton Bouton2 = new JButton("Rechercher un livre");
	    	Bouton2.addActionListener(new RechercherLivre(listeDelivres));
	    	panel.add(Bouton2, BorderLayout.SOUTH);
	    	
	    JButton Bouton3 = new JButton("Ajouter un livre");
	    	Bouton3.addActionListener(new AjouterLivre(listeDelivres));
	    	panel.add(Bouton3, BorderLayout.NORTH);
	    
	    JButton Bouton4 = new JButton("Supprimer un livre");
	    	Bouton4.addActionListener(new SupprimerLivre(listeDelivres,textField.getText()));
	    	panel.add(Bouton4, BorderLayout.EAST);
	    	
	    
	    JButton Bouton5 = new JButton("Afficher la liste");
	    	Bouton5.addActionListener(new Afficherliste(listeDelivres));
	    	panel.add(Bouton5, BorderLayout.CENTER);
	    	

	    	
	    	    		    	
	    this.setVisible(true);
	}
}
