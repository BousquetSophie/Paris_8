import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Collections;

public class fenetre_jeu extends JFrame {

    private int score;
    private ArrayList<String> commande;
    private ArrayList<String> preparation;
    private int tempsRestant = 60;
    private Timer timer;

    private JButton muffin, croissant, donut;
    private JButton cafe, chocolatChaud, pumpkinLatte, milkshakeMyrtille, milkshakeFramboise, theOrange;
    private ArrayList<JLabel> listeLabels;
    private JLabel c1, c2, c3, c4, c5, c6;
    private JLabel labelTempsRestant;

    public fenetre_jeu() {

        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        int screenWidth = screenSize.width;
        int screenHeight = screenSize.height;

        setSize(screenWidth, screenHeight);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);
        setUndecorated(true);

        String[] menu = {
            "Muffin", "Croissant", "Donut", "Café",
            "Chocolat chaud", "Latte", "Milkshake Myrtille", "Milkshake Framboise",
            "Thé à l'orange"
        };

        jeu jeu = new jeu();
        commande = jeu.commandeCafe(menu);
        preparation = new ArrayList<>();
        System.out.println("Objets choisis : " + commande);

        int largeurFenetre = getWidth();
        int hauteurFenetre = getHeight();
    
        double ratioLargeur = (double) largeurFenetre / 800; // 800 est la largeur de référence
        double ratioHauteur = (double) hauteurFenetre / 600;

        JPanel fond = new JPanel() {
            private Image imageDeFond = new ImageIcon("./image/fond_jeu.jpg").getImage();

            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.drawImage(imageDeFond, 0, 0, getWidth(), getHeight(), this);
            }
        };
        fond.setLayout(null);
        
        JButton gateaux = new JButton();
        gateaux.setBorderPainted(false);
        gateaux.setContentAreaFilled(false);
        gateaux.setFocusPainted(false);
        gateaux.setBounds((int)(0*ratioLargeur), (int)(220*ratioHauteur), (int)(120*ratioLargeur), (int)(150*ratioHauteur));

        JButton boisson = new JButton();
        boisson.setBorderPainted(false);
        boisson.setContentAreaFilled(false);
        boisson.setFocusPainted(false);
        boisson.setBounds((int)(720*ratioLargeur), (int)(160*ratioHauteur), (int)(80*ratioLargeur), (int)(120*ratioHauteur));

        JButton caisse = new JButton();
        caisse.setBorderPainted(false);
        caisse.setContentAreaFilled(false);
        caisse.setFocusPainted(false);
        caisse.setBounds((int)(260*ratioLargeur), (int)(270*ratioHauteur), (int)(130*ratioLargeur), (int)(200*ratioHauteur));

        JButton croix = new JButton(chargerEtRedimensionner("./image/croix.png", (int)(40*ratioLargeur), (int)(40*ratioLargeur)));
        croix.setBorderPainted(false);
        croix.setContentAreaFilled(false);
        croix.setFocusPainted(false);
        croix.setBounds(getWidth() - (int)(50*ratioLargeur), 10, (int)(40*ratioLargeur), (int)(40*ratioLargeur));

        JLabel labelScore = new JLabel("Score : " + String.valueOf(score));
        labelScore.setFont(new Font("Arial", Font.BOLD, (int)(20*ratioHauteur)));
        labelScore.setBounds(10, 10, (int)(200*ratioLargeur), (int)(40*ratioHauteur));
        labelScore.setForeground(Color.WHITE);

        muffin = new JButton(chargerEtRedimensionner("./image/muffin.png", (int)(60*ratioLargeur), (int)(60*ratioHauteur)));
        muffin.setBorderPainted(false);
        muffin.setFocusPainted(false);
        muffin.setBounds((int)(140*ratioLargeur), (int)(220*ratioHauteur), (int)(60*ratioLargeur), (int)(60*ratioHauteur));

        croissant = new JButton(chargerEtRedimensionner("./image/croissant.png", (int)(60*ratioLargeur), (int)(60*ratioHauteur)));
        croissant.setBorderPainted(false);
        croissant.setFocusPainted(false);
        croissant.setBounds((int)(140*ratioLargeur), (int)(290*ratioHauteur), (int)(60*ratioLargeur), (int)(60*ratioHauteur));

        donut = new JButton(chargerEtRedimensionner("./image/donut.png", (int)(60*ratioLargeur), (int)(60*ratioHauteur)));
        donut.setBorderPainted(false);
        donut.setFocusPainted(false);
        donut.setBounds((int)(140*ratioLargeur), (int)(360*ratioHauteur), (int)(60*ratioLargeur), (int)(60*ratioHauteur));

        cafe = new JButton(chargerEtRedimensionner("./image/cafe.png", (int)(55*ratioLargeur), (int)(80*ratioHauteur)));
        cafe.setBorderPainted(false);
        cafe.setFocusPainted(false);
        cafe.setBounds((int)(645*ratioLargeur), (int)(160*ratioHauteur), (int)(55*ratioLargeur), (int)(80*ratioHauteur));

        chocolatChaud = new JButton(chargerEtRedimensionner("./image/chocolatChaud.png", (int)(55*ratioLargeur), (int)(80*ratioHauteur)));
        chocolatChaud.setBorderPainted(false);
        chocolatChaud.setFocusPainted(false);
        chocolatChaud.setBounds((int)(645*ratioLargeur), (int)(255*ratioHauteur), (int)(55*ratioLargeur), (int)(80*ratioHauteur));

        pumpkinLatte = new JButton(chargerEtRedimensionner("./image/pumpkinLatte.png", (int)(55*ratioLargeur), (int)(80*ratioHauteur)));
        pumpkinLatte.setBorderPainted(false);
        pumpkinLatte.setFocusPainted(false);
        pumpkinLatte.setBounds((int)(645*ratioLargeur), (int)(345*ratioHauteur), (int)(55*ratioLargeur), (int)(80*ratioHauteur));

        milkshakeMyrtille = new JButton(chargerEtRedimensionner("./image/milkshakeMyrtille.png", (int)(55*ratioLargeur), (int)(80*ratioHauteur)));
        milkshakeMyrtille.setBorderPainted(false);
        milkshakeMyrtille.setFocusPainted(false);
        milkshakeMyrtille.setBounds((int)(575*ratioLargeur), (int)(160*ratioHauteur), (int)(55*ratioLargeur), (int)(80*ratioHauteur));

        milkshakeFramboise = new JButton(chargerEtRedimensionner("./image/milkshakeFramboise.png", (int)(55*ratioLargeur), (int)(80*ratioHauteur)));
        milkshakeFramboise.setBorderPainted(false);
        milkshakeFramboise.setFocusPainted(false);
        milkshakeFramboise.setBounds((int)(575*ratioLargeur), (int)(255*ratioHauteur), (int)(55*ratioLargeur), (int)(80*ratioHauteur));

        theOrange = new JButton(chargerEtRedimensionner("./image/theOrange.png", (int)(55*ratioLargeur), (int)(80*ratioHauteur)));
        theOrange.setBorderPainted(false);
        theOrange.setFocusPainted(false);
        theOrange.setBounds((int)(575*ratioLargeur), (int)(345*ratioHauteur), (int)(55*ratioLargeur), (int)(80*ratioHauteur));

        JLabel tableaux = new JLabel(chargerEtRedimensionner("./image/tableau.png", (int)(300*ratioLargeur), (int)(200*ratioHauteur)));
        tableaux.setBounds((int)(250*ratioLargeur), 0, (int)(300*ratioLargeur), (int)(200*ratioHauteur));

        listeLabels = new ArrayList<>();
        c1 = new JLabel("milkshake Framboise");
        c1.setFont(new Font("Arial", Font.PLAIN, (int)(18*ratioHauteur)));
        c1.setForeground(Color.WHITE);
        c1.setBounds((int)(300*ratioLargeur), (int)(30*ratioHauteur), (int)(250*ratioLargeur), (int)(20*ratioHauteur));
        listeLabels.add(c1);
        c2 = new JLabel("Label 2");
        c2.setFont(new Font("Arial", Font.PLAIN, (int)(18*ratioHauteur)));
        c2.setForeground(Color.WHITE);
        c2.setBounds((int)(300*ratioLargeur), (int)(50*ratioHauteur), (int)(250*ratioLargeur), (int)(20*ratioHauteur));
        listeLabels.add(c2);
        c3 = new JLabel("Label 3");
        c3.setFont(new Font("Arial", Font.PLAIN, (int)(18*ratioHauteur)));
        c3.setForeground(Color.WHITE);
        c3.setBounds((int)(300*ratioLargeur), (int)(70*ratioHauteur), (int)(250*ratioLargeur), (int)(20*ratioHauteur));
        listeLabels.add(c3);
        c4 = new JLabel("Label 4");
        c4.setFont(new Font("Arial", Font.PLAIN, (int)(18*ratioHauteur)));
        c4.setForeground(Color.WHITE);
        c4.setBounds((int)(300*ratioLargeur), (int)(90*ratioHauteur), (int)(250*ratioLargeur), (int)(20*ratioHauteur));
        listeLabels.add(c4);
        c5 = new JLabel("Label 5");
        c5.setFont(new Font("Arial", Font.PLAIN, (int)(18*ratioHauteur)));
        c5.setForeground(Color.WHITE);
        c5.setBounds((int)(300*ratioLargeur), (int)(110*ratioHauteur), (int)(250*ratioLargeur), (int)(20*ratioHauteur));
        listeLabels.add(c5);
        c6 = new JLabel("Label 6");
        c6.setFont(new Font("Arial", Font.PLAIN, (int)(18*ratioHauteur)));
        c6.setForeground(Color.WHITE);
        c6.setBounds((int)(300*ratioLargeur), (int)(130*ratioHauteur), (int)(250*ratioLargeur), (int)(20*ratioHauteur));
        listeLabels.add(c6);

        labelTempsRestant = new JLabel("Temps restant: 60s");
        labelTempsRestant.setFont(new Font("Arial", Font.BOLD, (int)(20*ratioHauteur)));
        labelTempsRestant.setBounds(10, 40, (int)(200*ratioLargeur), (int)(40*ratioHauteur));
        labelTempsRestant.setForeground(Color.WHITE);

        timer = new Timer(1000, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (tempsRestant > 0) {
                    tempsRestant--;
                    labelTempsRestant.setText("Temps restant: " + tempsRestant + "s");
                } else {
                    cacherGateaux();
                    cacherBoissons();
                    cacherLabel();

                    timer.stop();
                    if (score > 0){
                        score -= 100;
                    }

                    labelScore.setText("Score : " + score);
                    commande.clear();
                    preparation.clear();

                    commande = jeu.commandeCafe(menu);

                    for(int i = 0; i < commande.size(); i++)
                    {
                        listeLabels.get(i).setText(commande.get(i));
                        listeLabels.get(i).setVisible(true);
                    }

                    tempsRestant = 60;
                    labelTempsRestant.setText("Temps restant: 60s");
                    timer.restart();
                }
            }
        });

        timer.start();

        cacherGateaux();
        cacherBoissons();
        cacherLabel();

        for(int i = 0; i < commande.size(); i++)
        {
            listeLabels.get(i).setText(commande.get(i));
            listeLabels.get(i).setVisible(true);
        }

        fond.add(labelScore);
        fond.add(labelTempsRestant);
        fond.add(croix);
        fond.add(gateaux);
        fond.add(boisson);
        fond.add(caisse);
        fond.add(muffin);
        fond.add(croissant);
        fond.add(donut);
        fond.add(cafe);
        fond.add(chocolatChaud);
        fond.add(pumpkinLatte);
        fond.add(milkshakeMyrtille);
        fond.add(milkshakeFramboise);
        fond.add(theOrange);
        fond.add(c1);
        fond.add(c2);
        fond.add(c3);
        fond.add(c4);
        fond.add(c5);
        fond.add(c6);
        fond.add(tableaux);

        gateaux.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                muffin.setVisible(true);
                croissant.setVisible(true);
                donut.setVisible(true);
            }
        });

        boisson.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cafe.setVisible(true);
                chocolatChaud.setVisible(true);
                pumpkinLatte.setVisible(true);
                milkshakeMyrtille.setVisible(true);
                milkshakeFramboise.setVisible(true);
                theOrange.setVisible(true);
            }
        });

        caisse.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cacherGateaux();
                cacherBoissons();
                cacherLabel();

                Collections.sort(commande);
                Collections.sort(preparation);

                //System.out.println(commande);
                //System.out.println(preparation);

                boolean areEqual = commande.equals(preparation);

                if (areEqual) {
                    score += 100;
                } else if (score > 0){
                    score -= 100;
                }

                labelScore.setText("Score : " + score);

                commande.clear();
                preparation.clear();

                commande = jeu.commandeCafe(menu);

                for(int i = 0; i < commande.size(); i++)
                {
                    listeLabels.get(i).setText(commande.get(i));
                    listeLabels.get(i).setVisible(true);
                }

                tempsRestant = 60;
                labelTempsRestant.setText("Temps restant: 60s");
                timer.restart();
            }
        });

        croix.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
                int score_actuel = jeu.getScore("./score.txt");

                if (score > score_actuel) {
                    jeu.setScore(score, "./score.txt");
                }
            }
        });

        muffin.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cacherGateaux();
                preparation.add("Muffin");
            }
        });

        croissant.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cacherGateaux();
                preparation.add("Croissant");
            }
        });

        donut.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cacherGateaux();
                preparation.add("Donut");
            }
        });

        cafe.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cacherBoissons();
                preparation.add("Café");
            }
        });

        chocolatChaud.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cacherBoissons();
                preparation.add("Chocolat chaud");
            }
        });

        pumpkinLatte.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cacherBoissons();
                preparation.add("Latte");
            }
        });

        milkshakeMyrtille.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cacherBoissons();
                preparation.add("Milkshake Myrtille");
            }
        });

        milkshakeFramboise.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cacherBoissons();
                preparation.add("Milkshake Framboise");
            }
        });

        theOrange.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cacherBoissons();
                preparation.add("Thé à l'orange");
            }
        });
        setContentPane(fond);
    }

    private void cacherGateaux() {
        muffin.setVisible(false);
        croissant.setVisible(false);
        donut.setVisible(false);
    }

    private void cacherBoissons() {
        cafe.setVisible(false);
        chocolatChaud.setVisible(false);
        pumpkinLatte.setVisible(false);
        milkshakeMyrtille.setVisible(false);
        milkshakeFramboise.setVisible(false);
        theOrange.setVisible(false);
    }

    private void cacherLabel() {
        c1.setVisible(false);
        c2.setVisible(false);
        c3.setVisible(false);
        c4.setVisible(false);
        c5.setVisible(false);
        c6.setVisible(false);
    }

    private ImageIcon chargerEtRedimensionner(String chemin, int largeur, int hauteur) {
        ImageIcon icon = new ImageIcon(chemin);
        Image img = icon.getImage().getScaledInstance(largeur, hauteur, Image.SCALE_SMOOTH);
        return new ImageIcon(img);
    }    

    /*public static void main(String[] args) {
        fenetre_jeu jeu = new fenetre_jeu();
        jeu.setVisible(true);
    }*/
}
