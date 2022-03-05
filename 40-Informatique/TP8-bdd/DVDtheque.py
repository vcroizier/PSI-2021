# -*- coding: utf-8 -*-
"""
Cours NSI T sur les bases de données
Activité 6
"""

import sqlite3

chemin_vers_le_fichier_db = r"C:\Desktop" # A adapter avec votre chemin d'accès
nom_complet_du_fichier = chemin_vers_le_fichier_db + '\\' + 'DVDtheque.db'


def interrogation(requete: str) -> None:
    """
    Fonction exécutant et affichant les résultats de la requête SQL nommée
    "requete".
    """
    connexion = sqlite3.connect(nom_complet_du_fichier) 
    c = connexion.cursor()
    try:
        print('******************************************')
        c.execute( requete )
        for ligne in c.fetchall():
            print(ligne)
        print('******************************************')
    except :
        print("Erreur d'exécution pour la requête SQL")
    connexion.close()

  
#interrogation("SELECT * FROM Abonne") # exemple d'utilisation

