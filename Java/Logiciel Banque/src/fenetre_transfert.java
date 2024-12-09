package src;
import javax.swing.*;
import javax.swing.text.NumberFormatter;
import java.awt.*;
import java.awt.event.*;
import java.text.NumberFormat;

public class fenetre_transfert extends JFrame {
    
    public fenetre_transfert(compte_banquaire compte) {
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
        fond.setLayout(null); // Positionnement manuel des composants

        // Boutons
        JButton transfert = new JButton("Valider");
        transfert.setBounds(200, 600, 200, 50);
        JButton quitter = new JButton("Annuler");
        quitter.setBounds(200, 680, 200, 50);

        // Liste déroulante pour choisir entre dépôt et transfert
        String[] options = {"Transfert", "Dépôt"};
        JComboBox<String> comboBox = new JComboBox<>(options);
        comboBox.setBounds(150, 160, 200, 50);

        // Champs de texte
        JTextField num_id1 = new JTextField(20);
        num_id1.setText(compte.getId());
        num_id1.setEditable(false);
        num_id1.setBounds(150, 380, 350, 50);
        JTextField num_id2 = new JTextField(20);
        num_id2.setText("0000");
        num_id2.setBounds(150, 500, 350, 50);

        // Champ de texte formaté pour le montant
        NumberFormat format = NumberFormat.getNumberInstance();
        format.setGroupingUsed(false); // Pas de séparateurs de milliers
        NumberFormatter formatter = new NumberFormatter(format);
        formatter.setAllowsInvalid(false); // Empêche la saisie invalide
        formatter.setMinimum(0.0); // Minimum de 0
        JFormattedTextField montant = new JFormattedTextField(formatter);
        montant.setBounds(150, 280, 350, 50);

        // Labels
        JLabel labelTransfert1 = new JLabel("Depuis le compte");
        labelTransfert1.setBounds(150, 340, 200, 50);
        labelTransfert1.setForeground(Color.WHITE);
        JLabel labelTransfert2 = new JLabel("Vers le compte");
        labelTransfert2.setBounds(150, 460, 200, 50);
        labelTransfert2.setForeground(Color.WHITE);
        JLabel labelMontant = new JLabel("Montant");
        labelMontant.setBounds(150, 240, 200, 50);
        labelMontant.setForeground(Color.WHITE);
        JLabel labelInsuffidant = new JLabel("Votre solde est insuffisant");
        labelInsuffidant.setBounds(150, 210, 200, 50);
        JLabel montantInvalide = new JLabel("Montant invalide");
        montantInvalide.setBounds(150, 210, 200, 50);
        montantInvalide.setForeground(Color.WHITE);
        JLabel invalide = new JLabel("Le numéro d'identification n'existe pas");
        invalide.setBounds(150, 430, 300, 50);
        invalide.setForeground(Color.RED);

        // Bannière
        ImageIcon imageBanniere = new ImageIcon("./img/banque.png");
        Image imgBanniere = imageBanniere.getImage();
        Image banniereRedimensionnee = imgBanniere.getScaledInstance(600, 150, Image.SCALE_SMOOTH);
        ImageIcon imgBanierreR = new ImageIcon(banniereRedimensionnee);
        JLabel labelBanniere = new JLabel(imgBanierreR);
        labelBanniere.setBounds(0, 10, 600, 150);

        // Ajouter les composants au panneau
        fond.add(transfert);
        fond.add(quitter);
        fond.add(comboBox);
        fond.add(num_id1);
        fond.add(num_id2);
        fond.add(montant);
        fond.add(labelTransfert1);
        fond.add(labelTransfert2);
        fond.add(labelMontant);
        fond.add(labelInsuffidant);
        fond.add(montantInvalide);
        fond.add(invalide);
        fond.add(labelBanniere);

        // Griser ou activer les champs en fonction du choix
        comboBox.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String choix = (String) comboBox.getSelectedItem();
                if ("Dépôt".equals(choix)) {
                    montant.setEnabled(true);
                    num_id1.setEnabled(false);
                    num_id2.setEnabled(false);
                } else if ("Transfert".equals(choix)) {
                    montant.setEnabled(true);
                    num_id1.setEnabled(true);
                    num_id2.setEnabled(true);
                }
            }
        });

        transfert.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                invalide.setVisible(false);
                montantInvalide.setVisible(false);
                labelInsuffidant.setVisible(false);

                transfert t = new transfert();

                String choix = (String) comboBox.getSelectedItem();
                String compteDepuis = num_id1.getText();
                String compteVers = num_id2.getText();
                String montantText = montant.getText();
                int montantTextInt = Integer.parseInt(montantText);
                int soldeDuCompte = compte.getSolde();

                if ("Dépôt".equals(choix)) {
                    // Vérification du montant
                    if (montantText.isEmpty() || Double.parseDouble(montantText) <= 0) {
                        montantInvalide.setVisible(true);
                    } else {
                        String nouveauMontant = String.valueOf(soldeDuCompte + montantTextInt);
                        t.modifierMontant("./src/donnee_compte.txt", compte.getId() , nouveauMontant);
                        compte.ajouterSolde(montantTextInt);
                        
                        dispose();
                        fenetre_compte fenetre_compte = new fenetre_compte(compte);
                        fenetre_compte.setVisible(true);
                    }
                } else if ("Transfert".equals(choix)) {
                    // Vérifications pour le transfert
                    if (compteVers.isEmpty() || montantText.isEmpty() || Double.parseDouble(montantText) <= 0) {
                        montantInvalide.setVisible(true);
                    } else if ((soldeDuCompte-montantTextInt)<0) {
                        labelInsuffidant.setVisible(true);
                    } else if (compteDepuis.equals(compteVers) || (!(t.verif_id("./src/donnee_compte.txt", compteVers)))) {
                        invalide.setVisible(true);
                    } else {
                        String nouveauMontant1 = String.valueOf(soldeDuCompte-montantTextInt);
                        String montantCompteVers = t.recupererSolde("./src/donnee_compte.txt", compteVers);
                        int montantCompteVersI = Integer.parseInt(montantCompteVers);
                        String nouveauMontant2 = String.valueOf(montantCompteVersI+montantTextInt);

                        t.modifierMontant("./src/donnee_compte.txt", compteDepuis,nouveauMontant1);
                        t.modifierMontant("./src/donnee_compte.txt", compteVers, nouveauMontant2);

                        compte.retirerSolde(montantTextInt);

                        dispose();
                        fenetre_compte fenetre_compte = new fenetre_compte(compte);
                        fenetre_compte.setVisible(true);
                    }
                }
            }
        });

        // Bouton "Annuler"
        quitter.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
                fenetre_compte fenetre_compte = new fenetre_compte(compte);
                fenetre_compte.setVisible(true);
            }
        });
        
        invalide.setVisible(false);
        montantInvalide.setVisible(false);
        labelInsuffidant.setVisible(false);

        // Ajouter le panneau avec l'image de fond à la fenêtre
        setContentPane(fond);
    }
}
