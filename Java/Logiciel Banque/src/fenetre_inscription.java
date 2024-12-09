package src;
import javax.swing.*;
import javax.swing.text.NumberFormatter;

import java.awt.*;
import java.awt.event.*;
import java.io.FileWriter;
import java.io.IOException;
import java.text.NumberFormat;

public class fenetre_inscription extends JFrame {
    
    public fenetre_inscription() {
        setTitle("Inscription");
        setSize(600, 800);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        // Créer un JPanel avec une image de fond
        JPanel Fond = new JPanel() {
            private Image imageDeFond = new ImageIcon("./img/fond.jpg").getImage();

            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.drawImage(imageDeFond, 0, 0, getWidth(), getHeight(), this);
            }
        };
        Fond.setLayout(null); // Permet de positionner les composants manuellement

        // Boutons
        JButton inscription = new JButton("Inscription");
        inscription.setBounds(200, 640, 200, 50);
        JButton retour = new JButton("Retour");
        retour.setBounds(200, 700, 200, 50);

        // Champs de texte et mot de passe
        NumberFormat format = NumberFormat.getNumberInstance();
        format.setGroupingUsed(false); // Pas de séparateurs de milliers
        NumberFormatter formatter = new NumberFormatter(format);
        formatter.setAllowsInvalid(false); // Empêche la saisie invalide
        formatter.setMinimum(0.0); // Minimum de 0
        JFormattedTextField num_id = new JFormattedTextField(formatter);
        num_id.setBounds(150, 320, 350, 50);
        JPasswordField mdp = new JPasswordField(20);
        mdp.setBounds(150, 440, 350, 50);
        JPasswordField mdp_conf = new JPasswordField(20);
        mdp_conf.setBounds(150, 560, 350, 50);

        // Labels
        JLabel id_label = new JLabel("Numéro d'identification");
        id_label.setBounds(150, 280, 200, 50);
        id_label.setForeground(Color.WHITE);
        JLabel mdp_label = new JLabel("Mot De Passe");
        mdp_label.setBounds(150, 400, 200, 50);
        mdp_label.setForeground(Color.WHITE);
        JLabel mdp_labelConf = new JLabel("Confirmation du mot de passe");
        mdp_labelConf.setBounds(150, 520, 250, 50);
        mdp_labelConf.setForeground(Color.WHITE);
        JLabel invalide = new JLabel("Identifiant déjà existant");
        invalide.setBounds(150, 250, 500, 50);
        JLabel invalide_mdp = new JLabel("Le mot de passe ne correspond pas");
        invalide_mdp.setBounds(150, 500, 500, 50);
        invalide_mdp.setForeground(Color.RED);

        // Image de profil
        ImageIcon imageProfil = new ImageIcon("./img/profil.png");
        Image imgProfil = imageProfil.getImage();
        Image profilRedimensionnee = imgProfil.getScaledInstance(230, 230, Image.SCALE_SMOOTH);
        ImageIcon imgProfilR = new ImageIcon(profilRedimensionnee);
        JLabel labelProfil = new JLabel(imgProfilR);
        labelProfil.setBounds(190, 25, 230, 230);

        // Ajouter les composants au panneau
        Fond.add(inscription);
        Fond.add(retour);
        Fond.add(num_id);
        Fond.add(mdp);
        Fond.add(mdp_conf);
        Fond.add(id_label);
        Fond.add(mdp_label);
        Fond.add(mdp_labelConf);
        Fond.add(invalide);
        Fond.add(invalide_mdp);
        Fond.add(labelProfil);

        invalide.setVisible(false);
        invalide_mdp.setVisible(false);

        inscription.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                invalide.setVisible(false);
                invalide_mdp.setVisible(false);
                
                String username = num_id.getText();

                char[] mdpChar1 = mdp.getPassword();
                String motDePasse = new String(mdpChar1);

                char[] mdpChar2 = mdp_conf.getPassword();
                String motDePasseConf = new String(mdpChar2);

                inscription i = new inscription();

                if(i.verif_id("./src/donnee_compte.txt",username))
                    invalide.setVisible(true);

                else if (!(i.verif_mdp(motDePasse,motDePasseConf)))
                    invalide_mdp.setVisible(true);

                else {
                    compte_banquaire compte = new compte_banquaire(username, motDePasse, 100);
                    dispose();

                    //ajouter les données au fichier
                    String cheminFichier = "./src/donnee_compte.txt";
                    String ligneAAjouter = username + "," + motDePasse + ",100\n";

                    try (FileWriter writer = new FileWriter(cheminFichier, true)) {
                        writer.write(ligneAAjouter);
                        System.out.println("Ligne ajoutée avec succès.");
                    } catch (IOException f) {
                        System.err.println("Erreur lors de l'ajout de la ligne : " + f.getMessage());
                    }

                    fenetre_compte fenetreCompte = new fenetre_compte(compte);
                    fenetreCompte.setVisible(true);
                }
            }
        });
        
        retour.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
                fenetre_loging fenetreLoging = new fenetre_loging();
                fenetreLoging.setVisible(true);
            }
        });

        // Ajouter le panneau avec l'image de fond à la fenêtre
        setContentPane(Fond);
    }
}
