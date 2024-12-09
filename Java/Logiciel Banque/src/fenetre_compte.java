package src;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class fenetre_compte extends JFrame {
    
    public fenetre_compte(compte_banquaire compte) {
        //setTitle("Compte");
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
        JButton transfert = new JButton("Transfert");
        transfert.setBounds(200, 530, 200, 50);
        JButton deconnexion = new JButton("Déconnexion");
        deconnexion.setBounds(200, 620, 200, 50);

        // Labels
        String solde = String.valueOf(compte.getSolde());
        JLabel labelSolde = new JLabel(solde);
        labelSolde.setBounds(170, 250, 200, 100);
        labelSolde.setFont(new Font("Arial", Font.PLAIN, 30));
        labelSolde.setForeground(Color.WHITE);

        // Bannière
        ImageIcon imageBanniere = new ImageIcon("./img/banque.png");
        Image imgBanniere = imageBanniere.getImage();
        Image banniereRedimensionnee = imgBanniere.getScaledInstance(600, 150, Image.SCALE_SMOOTH);
        ImageIcon imgBanierreR = new ImageIcon(banniereRedimensionnee);
        JLabel labelBanniere = new JLabel(imgBanierreR);
        labelBanniere.setBounds(0, 10, 600, 150);

        // Carte
        ImageIcon imageCarte = new ImageIcon("./img/carte.png");
        Image imgCarte = imageCarte.getImage();
        Image carteRedimensionnee = imgCarte.getScaledInstance(500, 500, Image.SCALE_SMOOTH);
        ImageIcon imgCarteR = new ImageIcon(carteRedimensionnee);
        JLabel labelCarte = new JLabel(imgCarteR);
        labelCarte.setBounds(20, 100, 500, 500);

        // Ajouter les composants au panneau
        fond.add(transfert);
        fond.add(deconnexion);
        fond.add(labelSolde);
        fond.add(labelBanniere);
        fond.add(labelCarte);

        transfert.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
                fenetre_transfert fentreTransfert = new fenetre_transfert(compte);
                fentreTransfert.setVisible(true);
            }
        });

        deconnexion.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
            }
        });
        
        // Ajouter le panneau avec l'image de fond à la fenêtre
        setContentPane(fond);
    }
}
