import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Iterator;
import java.util.Map;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class RechercherLivre implements ActionListener {
	protected ListeDeLivres listeDelivres;
	protected RechercherLivre(ListeDeLivres listeDelivres) {
		this.listeDelivres=listeDelivres;
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		Iterator<Map.Entry<String, Livre>> iter = this.listeDelivres.Dico.entrySet().iterator();		
		while(iter.hasNext())
		{
			Map.Entry<String, Livre> entr = iter.next();
			if (entr.getValue().getCode().equals(Fenetre.textField.getText()))
			{
				System.out.println("Le livre existe !");
				entr.getValue().afficheLivre();
			
			}
		} 

	}

}
