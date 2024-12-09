package src;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class inscription {

    public boolean verif_id(String fichier, String identifiantRecherche) {
        try (BufferedReader reader = new BufferedReader(new FileReader(fichier))) {
            String ligne;
            
            while ((ligne = reader.readLine()) != null) {
                String[] i = ligne.split(",");
                if (i[0].equals(identifiantRecherche)) {
                    return true;
                }
            }
            
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Erreur lors de la lecture du fichier");
        }
        
        return false;
    }

    public boolean verif_mdp(String mdp, String mdpConf)
    {
        return mdp.equals(mdpConf);
    }
}
