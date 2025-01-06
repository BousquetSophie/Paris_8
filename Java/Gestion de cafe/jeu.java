import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;

public class jeu {
    
    public int getScore(String fichier)
    {
        try (BufferedReader reader = new BufferedReader(new FileReader(fichier))) {
            String ligne = reader.readLine();
            reader.close();
            int score = Integer.parseInt(ligne);
            return score;
            
        } catch (IOException e) {
            System.err.println("Erreur lors de l'ouverture du fichier " + e.getMessage());
        }

        return 0;
    }

    public void setScore(int score, String fichier)
    {
        try (FileWriter writer = new FileWriter(fichier)) {
            writer.write(String.valueOf(score));
        } catch (IOException e) {
            System.err.println("Erreur lors de la modification du score" + e.getMessage());
        }
    }

    public ArrayList<String> commandeCafe(String[] objets) {
        Random random = new Random();
        ArrayList<String> resultat = new ArrayList<String>();

        // Nombre aléatoire entre 1 et 6
        int nombreAleatoire = random.nextInt(6) + 1;

        for (int i = 0; i < nombreAleatoire; i++) {
            int indexAleatoire = random.nextInt(objets.length);
            resultat.add(objets[indexAleatoire]);
        }

        return resultat;
    }

    /*public static void main(String[] args) {
        // Liste de 12 objets
        String[] objets = {
            "Objet 1", "Objet 2", "Objet 3", "Objet 4",
            "Objet 5", "Objet 6", "Objet 7", "Objet 8",
            "Objet 9", "Objet 10", "Objet 11", "Objet 12"
        };

        // Appel de la fonction
        ArrayList<String> objetsChoisis = commandeCafe(objets);

        // Affichage des objets choisis
        System.out.println("Objets choisis : " + objetsChoisis);
    }*/
}
