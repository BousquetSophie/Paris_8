package src;

public class compte_banquaire {
    private String id;
    private String mdp;
    private int solde;

    public compte_banquaire(String i, String m, int s)
    {
        id = i;
        mdp = m;
        solde = s;
    }

    public String getId()
    {
        return id;
    }
    public String getMdp()
    {
        return mdp;
    }
    public int getSolde()
    {
        return solde;
    }
    public void ajouterSolde(int i)
    {
        solde = solde + i;
    }
    public void retirerSolde(int i)
    {
        solde = solde - i;
    }

}

