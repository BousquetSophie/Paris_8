-- Création de la table Utilisateurs
CREATE TABLE Utilisateurs (
    ID INT PRIMARY KEY,
    Nom VARCHAR(50),
    Age INT
);

-- Insertion de données d'exemple dans la table Utilisateurs
INSERT INTO Utilisateurs (ID, Nom, Age) 
VALUES
(1, 'Alice', 30),
(2, 'Bob', 35),
(3, 'Charlie', 25),
(4, 'David', 40);

-- Création de la table Commandes
CREATE TABLE Commandes (
    ID INT PRIMARY KEY,
    ID_Utilisateur INT,
    Montant DECIMAL(10, 2),
    FOREIGN KEY (ID_Utilisateur) REFERENCES Utilisateurs(ID)
);

-- Insertion de données d'exemple dans la table Commandes
INSERT INTO Commandes (ID, ID_Utilisateur, Montant) 
VALUES
(1, 1, 100.00),
(2, 1, 150.00),
(3, 2, 200.00),
(4, 3, 80.00),
(5, 4, 120.00);

-- Requête pour trouver les noms des utilisateurs ayant passé des commandes dont le montant total est supérieur à la moyenne des montants de toutes les commandes
SELECT DISTINCT u.Nom 
FROM Utilisateurs u
JOIN Commandes c ON u.ID = c.ID_Utilisateur
WHERE c.Montant > (
    SELECT AVG(Montant)
    FROM Commandes
);
