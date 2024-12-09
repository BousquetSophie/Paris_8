package src;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class connexion {
    private String mdp;
    private String montant;

    public boolean verif_id(String fichier, String identifiantRecherche) {
        try (BufferedReader reader = new BufferedReader(new FileReader(fichier))) {
            String ligne;
            
            while ((ligne = reader.readLine()) != null) {
                String[] i = ligne.split(",");
                if (i[0].equals(identifiantRecherche)) {
                    this.mdp = i[1];
                    this.montant = i[2];
                    return true;
                }
            }
            
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Erreur lors de la lecture du fichier.");
        }

        this.mdp = null;
        this.montant = null;
        return false;
    }
    
    public boolean verif_mdp(String motDePasse) {
        return mdp != null && mdp.equals(motDePasse);
    }

    public String getMontant() {
        return montant;
    }
}
