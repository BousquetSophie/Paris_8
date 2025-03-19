import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class ajouter_contact extends JFrame {
    
    public ajouter_contact() {
        setSize(600, 800);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        JPanel fond = new JPanel() {
            private Image imageDeFond = new ImageIcon("./image/fond.jpg").getImage();

            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.drawImage(imageDeFond, 0, 0, getWidth(), getHeight(), this);
            }
        };
        fond.setLayout(null);

        JLabel profil = new JLabel(chargerEtRedimensionner("./image/profil.png", 200, 200));
        profil.setBounds(180, 40, 200, 200);

        JLabel ImgPerso = new JLabel(chargerEtRedimensionner("./image/contact.png", 50, 50));
        ImgPerso.setBounds(100, 300, 50, 50);
        JTextField nom = new JTextField(300);
        nom.setFont(new Font("Serif", Font.BOLD, 20));
        nom.setBounds(200, 300, 300, 50);

        JLabel ImgTel = new JLabel(chargerEtRedimensionner("./image/telephone.png", 50, 50));
        ImgTel.setBounds(100, 400, 50, 50);
        JTextField telephone = new JTextField(30);
        telephone.setFont(new Font("Serif", Font.BOLD, 20));
        telephone.setBounds(200, 400, 300, 50);

        JLabel ImgMail = new JLabel(chargerEtRedimensionner("./image/mail.png", 50, 50));
        ImgMail.setBounds(100, 500, 50, 50);
        JTextField mail = new JTextField(300);
        mail.setFont(new Font("Serif", Font.BOLD, 20));
        mail.setBounds(200, 500, 300, 50);

        JButton enregistrer = new JButton("Enregistrer");
        enregistrer.setBounds(220, 620, 120, 50);

        fond.add(profil);
        fond.add(ImgPerso);
        fond.add(nom);
        fond.add(ImgTel);
        fond.add(telephone);
        fond.add(ImgMail);
        fond.add(mail);
        fond.add(enregistrer);

        enregistrer.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String n = nom.getText();
                String t = telephone.getText();
                String m = mail.getText();

                enregistrerContact(n, t, m);

                dispose();

                page_accueil page_accueil = new page_accueil();
            }
        });

        setContentPane(fond);
        setVisible(true);
    }

    private void enregistrerContact(String nom, String telephone, String mail) {
        Connection conn = null;
        PreparedStatement pstmt = null;
        
        try {
            conn = DriverManager.getConnection("jdbc:sqlite:baseDeDonnees.db");

            String sql = "INSERT INTO contact (nom, telephone, mail) VALUES (?, ?, ?)";
            pstmt = conn.prepareStatement(sql);
            
            pstmt.setString(1, nom);
            pstmt.setString(2, telephone);
            pstmt.setString(3, mail);

            pstmt.executeUpdate();
            
            JOptionPane.showMessageDialog(this, "Contact ajouté avec succès !");
        } catch (SQLException e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "Erreur lors de l'ajout du contact.");
        } finally {
            try {
                if (pstmt != null) pstmt.close();
                if (conn != null) conn.close();
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
        }
    }

    private ImageIcon chargerEtRedimensionner(String chemin, int largeur, int hauteur) {
        ImageIcon icon = new ImageIcon(chemin);
        Image img = icon.getImage().getScaledInstance(largeur, hauteur, Image.SCALE_SMOOTH);
        return new ImageIcon(img);
    }
}
