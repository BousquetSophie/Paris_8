import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Afficherliste implements ActionListener {
	protected ListeDeLivres listeDelivres;
	protected Afficherliste(ListeDeLivres listeDelivres) {
		this.listeDelivres=listeDelivres;
	}
	public void actionPerformed(ActionEvent e)
	{
		
		listeDelivres.afficherLesLivres();
	}

}
