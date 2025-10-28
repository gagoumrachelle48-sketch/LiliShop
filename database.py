# database.py
import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Mabellerachou@93",  # Mot de passe MySQL
    "database": "lilishop"           # Nom de la base
}

def get_connection():
    """
    Établit et retourne une connexion MySQL.
    Affiche un message clair en cas d'erreur.
    """
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
        else:
            raise Error("⚠️ La connexion MySQL n'a pas pu être établie.")
    except Error as e:
        print("⚠️ Erreur de connexion MySQL :", e)
        return None



#import est un mot cle de python qui permet d'inclure un module externe (une bibiotheque de fonction)
#mysql.connector est le module de python qui permet de cd connecter rt d'interagir avec une base de donnees mysql
#import mysql.connector

#def est un mot cle qui definit une nouvelle fonction (une sequence d'instructions reutilisable).
#get_connection est le nom de ceete fonction.son role est de renvoyer(return) un objet de connexion a la base de donnees
#def get_connection():
    #return mysql.connector.connect(   #return  est le mot cle qui definit une nouvelle fonction(une sequence d'instructions reutilisable)  et mysql.connector.connect appelle la fpnction de connection du module
    #host="localhost",                 #host="localhost":specifie l'adresse du serveur de base de donnees
    #user="root",                      #user="root: specifiele nom d'utlisateur MySQL a l'utiliser pour la connexion c'est generalement utiliser comme administrateur par defaut
   # password="Mabellerachou@93",      #password ="Mabellerachou@93" formit le mot de basse de l'utilisateur MySQL qui doit etre remplacer par le vrai mot de passe 
    #database="LiliShop_db",           #database="LiliShop_db" specifie le nom exactde la base de donnees a laquelle se connecter
  #  )
  


    
