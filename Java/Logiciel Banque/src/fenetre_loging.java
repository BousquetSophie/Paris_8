
package src;
import javax.swing.*;
import javax.swing.text.NumberFormatter;

import java.awt.*;
import java.awt.event.*;
import java.text.NumberFormat;

public class fenetre_loging extends JFrame {
    
    public fenetre_loging() {
        setTitle("Loging");
        setSize(600, 800);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        // Créer un JPanel avec une image de fond
        JPanel fond = new JPanel() {
            private Image imageDeFond = new ImageIcon("./img/fond.jpg").getImage();

            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.drawImage(imageDeFond, 0, 0, getWidth(), getHeight(), this);
            }
        };
        fond.setLayout(null); // Permet de positionner les composants manuellement

        // Boutons
        JButton connexion = new JButton("Connexion");
        connexion.setBounds(200, 540, 200, 50);
        JButton inscription = new JButton("Inscription");
        inscription.setBounds(200, 620, 200, 50);

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

        // Labels
        JLabel id_label = new JLabel("Numéro d'identification");
        id_label.setBounds(150, 280, 200, 50);
        id_label.setForeground(Color.WHITE);
        
        JLabel mdp_label = new JLabel("Mot De Passe");
        mdp_label.setBounds(150, 400, 200, 50);
        mdp_label.setForeground(Color.WHITE);
        JLabel invalide = new JLabel("Identifiant ou mot de passe invalide");
        invalide.setBounds(150, 250, 500, 50);

        // Image de profil
        ImageIcon imageProfil = new ImageIcon("./img/profil.png");
        Image imgProfil = imageProfil.getImage();
        Image profilRedimensionnee = imgProfil.getScaledInstance(230, 230, Image.SCALE_SMOOTH);
        ImageIcon imgProfilR = new ImageIcon(profilRedimensionnee);
        JLabel labelProfil = new JLabel(imgProfilR);
        labelProfil.setBounds(190, 25, 230, 230);

        // Ajouter les composants au panneau
        fond.add(connexion);
        fond.add(inscription);
        fond.add(num_id);
        fond.add(mdp);
        fond.add(id_label);
        fond.add(mdp_label);
        fond.add(invalide);
        fond.add(labelProfil);

        invalide.setVisible(false);

        connexion.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                invalide.setVisible(false);
                String identifiant = num_id.getText();

                char[] mdpChar = mdp.getPassword();
                String motDePasse = new String(mdpChar);

                connexion loging = new connexion();

                if(!(loging.verif_id("./src/donnee_compte.txt", identifiant)))
                    invalide.setVisible(true);
                else if(!(loging.verif_mdp(motDePasse)))
                    invalide.setVisible(true);
                else{
                    String montant = loging.getMontant();
                    int montantInt = Integer.parseInt(montant);
                    compte_banquaire compte_banquaire = new compte_banquaire(identifiant, motDePasse, montantInt);
                    dispose();
                    fenetre_compte fenetre_compte = new fenetre_compte(compte_banquaire);
                    fenetre_compte.setVisible(true);
                }
            }
        });
        
        inscription.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose(); // Ferme la fenêtre actuelle
                fenetre_inscription fenetreInscription = new fenetre_inscription();
                fenetreInscription.setVisible(true);
            }
        });

        // Ajouter le panneau avec l'image de fond à la fenêtre
        setContentPane(fond);
    }
}
