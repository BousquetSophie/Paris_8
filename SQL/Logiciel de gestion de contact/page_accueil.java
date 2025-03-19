import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.sql.*;

public class page_accueil extends JFrame {
    
    public page_accueil() {
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

        JLabel label1 = new JLabel("Contacts");
        label1.setFont(new Font("Serif", Font.BOLD, 45));
        label1.setBounds(170, 40, 300, 100);

        JFormattedTextField recherche = new JFormattedTextField();
        recherche.setBounds(95, 195, 300, 30);

        JButton loupe = new JButton(chargerEtRedimensionner("./image/loupe.png", 40, 40));
        loupe.setBorderPainted(false);
        loupe.setContentAreaFilled(false);
        loupe.setFocusPainted(false);
        loupe.setBounds(30, 190, 40, 40);

        JButton plus = new JButton(chargerEtRedimensionner("./image/plus.png", 30, 30));
        plus.setBorderPainted(false);
        plus.setContentAreaFilled(false);
        plus.setFocusPainted(false);
        plus.setBounds(500, 195, 30, 30);

        JPanel contactMenu = new JPanel();
        contactMenu.setLayout(new GridLayout(0, 1, 5, 5));
        chargerContacts(contactMenu, "");

        JScrollPane menuDeroulant = new JScrollPane(contactMenu);
        menuDeroulant.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        menuDeroulant.setBounds(70, 300, 450, 450);

        fond.add(loupe);
        fond.add(recherche);
        fond.add(label1);
        fond.add(plus);
        fond.add(menuDeroulant);

        plus.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
                ajouter_contact ajouter_contact = new ajouter_contact();
                ajouter_contact.setVisible(true);
            }
        });

        loupe.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String texteRecherche = recherche.getText().trim();
                chargerContacts(contactMenu, texteRecherche);
            }
        });
        

        setContentPane(fond);
        setVisible(true);
    }

    private void chargerContacts(JPanel contactMenu, String filtre) {
        contactMenu.removeAll();
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
    
        try {
            conn = DriverManager.getConnection("jdbc:sqlite:baseDeDonnees.db");
    
            String sql = "SELECT id, nom, telephone, mail FROM contact WHERE nom LIKE ?";
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, "%" + filtre + "%");
    
            rs = pstmt.executeQuery();
    
            while (rs.next()) {
                int id = rs.getInt("id");
                String nom = rs.getString("nom");
                String telephone = rs.getString("telephone");
                String mail = rs.getString("mail");
    
                JPanel RectContact = new JPanel();
                RectContact.setLayout(new GridLayout(4, 1));
                RectContact.setBorder(BorderFactory.createLineBorder(Color.BLACK));
                RectContact.setBackground(Color.LIGHT_GRAY);
    
                JLabel nomLabel = new JLabel(nom, SwingConstants.CENTER);
                JLabel telLabel = new JLabel(telephone, SwingConstants.CENTER);
                JLabel mailLabel = new JLabel(mail, SwingConstants.CENTER);
    
                JButton supprimerBtn = new JButton(chargerEtRedimensionner("./image/poubelle.png", 20, 20));
                supprimerBtn.setBorderPainted(false);
                supprimerBtn.setContentAreaFilled(false);
                supprimerBtn.setFocusPainted(false);

                supprimerBtn.addActionListener(e -> {
                    supprimerContact(id);
                    chargerContacts(contactMenu, filtre);
                });
    
                RectContact.add(nomLabel);
                RectContact.add(telLabel);
                RectContact.add(mailLabel);
                RectContact.add(supprimerBtn);
    
                contactMenu.add(RectContact);
            }
    
            contactMenu.revalidate();
            contactMenu.repaint();
    
        } catch (SQLException e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "Erreur lors du chargement des contacts.");
        } finally {
            try {
                if (rs != null) rs.close();
                if (pstmt != null) pstmt.close();
                if (conn != null) conn.close();
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
        }
    }    
    
    private void supprimerContact(int id) {
        Connection conn = null;
        PreparedStatement pstmt = null;
    
        try {
            conn = DriverManager.getConnection("jdbc:sqlite:baseDeDonnees.db");
            String sql = "DELETE FROM contact WHERE id = ?";
            pstmt = conn.prepareStatement(sql);
            pstmt.setInt(1, id);
            pstmt.executeUpdate();
    
            JOptionPane.showMessageDialog(this, "Contact supprimé avec succès.");
        } catch (SQLException e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "Erreur lors de la suppression du contact.");
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

    public static void main(String[] args) {
        new page_accueil();
    }
}
