public class Main {
    public static void main(String[] args) {
        ListeDeLivres listeDeLivres = new ListeDeLivres(null);

        Fenetre fenetre = new Fenetre(listeDeLivres);

        fenetre.setVisible(true);
    }
}
