import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class fenetre_start extends JFrame {

    public fenetre_start(){
        
        setSize(650, 800);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);
        //setUndecorated(true);

        JPanel fond = new JPanel() {
            private Image imageDeFond = new ImageIcon("./image/fond_cafe.jpg").getImage();

            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.drawImage(imageDeFond, 0, 0, getWidth(), getHeight(), this);
            }
        };
        fond.setLayout(null);

        ImageIcon imagestart = new ImageIcon("./image/start.png");
        Image imgstart = imagestart.getImage();
        Image startRedimensionnee = imgstart.getScaledInstance(150, 150, Image.SCALE_SMOOTH);
        ImageIcon imgstartR = new ImageIcon(startRedimensionnee);
        JButton start = new JButton(imgstartR);
        start.setBorderPainted(false);
        start.setContentAreaFilled(false);
        start.setFocusPainted(false);
        start.setBounds(270, 20, 150, 150);

        jeu jeu = new jeu();
        int scoreI = jeu.getScore("./score.txt");
        String score = String.valueOf(scoreI);

        JLabel labelScore = new JLabel("Meilleur score : " + score);
        labelScore.setFont(new Font("Arial", Font.BOLD, 20));
        labelScore.setBounds(10, 10, 400, 30);
        labelScore.setForeground(Color.WHITE);

        fond.add(start);
        fond.add(labelScore);

        start.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
                fenetre_jeu jeu = new fenetre_jeu();
                jeu.setVisible(true);
            }
        });

        setContentPane(fond);
    }

    public static void main(String[] args) {
        fenetre_start start = new fenetre_start();
        start.setVisible(true);
    }
}