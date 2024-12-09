package src;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class transfert {

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

    public String recupererSolde(String fichier, String identifiant) {
        try (BufferedReader reader = new BufferedReader(new FileReader(fichier))) {
            String ligne;
            
            // Lecture du fichier et recherche du solde correspondant
            while ((ligne = reader.readLine()) != null) {
                String[] i = ligne.split(",");
                if (i[0].equals(identifiant)) {
                    return i[2];
                }
            }
        } catch (IOException e) {
            System.out.println("Erreur lors de la lecture du fichier");
        }

        return null;
    }

    public void modifierMontant(String fichier, String identifiant, String nouveauMontant) {
        List<String> lignes = new ArrayList<>();
        
        try (BufferedReader reader = new BufferedReader(new FileReader(fichier))) {
            String ligne;
            
            // Lecture du fichier et modification de la ligne correspondante
            while ((ligne = reader.readLine()) != null) {
                String[] i = ligne.split(",");
                if (i[0].equals(identifiant)) {
                    // Modifier le montant dans la ligne
                    ligne = i[0] + "," + i[1] + "," + nouveauMontant;
                }
                lignes.add(ligne);
            }
            
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Erreur lors de la lecture du fichier");
            return;
        }

        // Réécriture de tout le fichier avec la liste modifiée
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fichier))) {
            for (String l : lignes) {
                writer.write(l);
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Erreur lors de l'écriture dans le fichier");
        }
    }
}
