import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;

public class SupprimerLivre implements ActionListener {

	protected ListeDeLivres listeDelivres;
	protected String code;
	public SupprimerLivre(ListeDeLivres listeDelivres,String code) {
		this.listeDelivres=listeDelivres;
		this.code=code;
	}

	public void actionPerformed(ActionEvent e)
	{
			
				
		Iterator<Map.Entry<String, Livre>> iter = this.listeDelivres.Dico.entrySet().iterator();		
		while(iter.hasNext())
		{
			Map.Entry<String, Livre> entr = iter.next();
			if (entr.getValue().getCode().equals(Fenetre.textField.getText()))
			{
				System.out.println("Livre supprim�");
				iter.remove();
			
			}
		} 
				
				
		

	}


}
