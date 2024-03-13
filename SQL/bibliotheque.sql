-- Création de la table Auteurs
CREATE TABLE IF NOT EXISTS Auteurs (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nom TEXT NOT NULL,
    Nationalite TEXT
);

-- Création de la table Livres
CREATE TABLE IF NOT EXISTS Livres (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Titre TEXT NOT NULL,
    Auteur_ID INTEGER,
    Année_Publication INTEGER,
    FOREIGN KEY (Auteur_ID) REFERENCES Auteurs(ID)
);

-- Création de la table Emprunts
CREATE TABLE IF NOT EXISTS Emprunts (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Livre_ID INTEGER,
    Date_Emprunt DATE,
    Date_Retour DATE,
    FOREIGN KEY (Livre_ID) REFERENCES Livres(ID)
);

-- Insertion de données d'exemple dans la table Auteurs
INSERT INTO Auteurs (Nom, Nationalite) VALUES
('Victor Hugo', 'Française'),
('William Shakespeare', 'Anglaise'),
('Fyodor Dostoevsky', 'Russe');

-- Insertion de données d'exemple dans la table Livres
INSERT INTO Livres (Titre, Auteur_ID, Année_Publication) VALUES
('Les Misérables', 1, 1862),
('Hamlet', 2, 1603),
('Crime and Punishment', 3, 1866);

-- Insertion de données d'exemple dans la table Emprunts
INSERT INTO Emprunts (Livre_ID, Date_Emprunt, Date_Retour) VALUES
(1, '2024-02-15', '2024-03-10'),
(2, '2024-01-10', '2024-01-25'),
(3, '2023-12-01', '2024-01-15');

-- Sélectionner tous les auteurs
SELECT * FROM Auteurs;

-- Sélectionner tous les livres
SELECT * FROM Livres;

-- Sélectionner tous les emprunts
SELECT * FROM Emprunts;
