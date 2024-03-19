import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Iterator;
import java.util.Map;

class AfficherLivre implements ActionListener   {
	protected ListeDeLivres listeDelivres;
	public AfficherLivre(ListeDeLivres listeDelivres) {
		this.listeDelivres=listeDelivres;
	}

    public void actionPerformed(ActionEvent e)
	{
    	Iterator<Map.Entry<String, Livre>> iter = this.listeDelivres.Dico.entrySet().iterator();		
		while(iter.hasNext())
		{
			Map.Entry<String, Livre> entr = iter.next();
			if (entr.getValue().getCode().equals(Fenetre.textField.getText()))
			{
				entr.getValue().afficheLivre();
			
			}
		} 
    	
    }



}
