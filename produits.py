# produits.py
from database import get_connection

def ajouter_produit():
    print("\n=== Ajouter un produit ===")
    nom = input("Nom du produit : ").strip()
    if not nom:
        print("❌ Le nom du produit ne peut pas être vide.")
        return

    try:
        prix = float(input("Prix du produit (€) : "))
        if prix <= 0:
            print("❌ Le prix doit être supérieur à 0.")
            return
    except ValueError:
        print("❌ Veuillez entrer un prix valide.")
        return

    try:
        stock = int(input("Quantité en stock : "))
        if stock < 0:
            print("❌ Le stock ne peut pas être négatif.")
            return
    except ValueError:
        print("❌ Veuillez entrer un nombre entier pour le stock.")
        return

    conn = get_connection()
    cur = conn.cursor()
    try:
        # Vérifier si le produit existe déjà
        cur.execute("SELECT id FROM produits WHERE nom = %s", (nom,))
        if cur.fetchone():
            print("❌ Ce produit existe déjà.")
            return

        cur.execute(
            "INSERT INTO produits (nom, prix, stock) VALUES (%s, %s, %s)",
            (nom, prix, stock)
        )
        conn.commit()
        print(f"✅ Produit '{nom}' ajouté avec succès !")
    except Exception as e:
        print("⚠️ Une erreur est survenue :", e)
    finally:
        cur.close()
        conn.close()

def voir_produits():
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, nom, prix, stock FROM produits ORDER BY nom ASC")
        produits = cur.fetchall()
        if not produits:
            print("⚠️ Aucun produit disponible.")
            return []

        print("\n--- Liste des produits ---")
        for p in produits:
            print(f"{p[0]} - {p[1]} : {p[2]:.2f} € (Stock: {p[3]})")
        return produits
    except Exception as e:
        print("⚠️ Une erreur est survenue :", e)
        return []
    finally:
        cur.close()
        conn.close()




#importe (rend disponible) la fonction 'get_connection'depuis le module 'database.py
#from database import get_connection 

# Définit une fonction nommée 'ajouter_produit'. C'est le début du processus.
#def ajouter_produit():
    ##conn = get_connection()  # Appelle la fonction importée pour établir la connexion au serveur MySQL. 'conn' stocke l'objet de connexion.
   # cur = conn.cursor()       # Crée un objet 'cursor' (curseur). Le curseur est l'outil nécessaire pour envoyer des commandes SQL au serveur.
   # nom = input("nom du produit :") # Demande à l'utilisateur d'entrer le nom du produit et stocke la réponse dans la variable 'nom'.
   # prix = float(input("prix(£) : "))  # Demande le prix et le convertit immédiatement en un nombre à virgule ('float').
    #stock = int(input("quantite en stock : "))  # Demande la quantité en stock et la convertit en un nombre entier ('int')
    #cur.execute("INSERT INTO produits (nom, prix, stock) VALUES (%s, %s, %s)", (nom, prix,stock))
 # 'cur.execute(...)' exécute une commande SQL. 
# Le SQL est une requête d'insertion (INSERT) des données collectées dans la table 'produits'. 
# Les '%s' sont des *placeholders* (marqueurs de position) pour insérer les variables Python en toute sécurité.
    #conn.commit()  # 'conn.commit()' : Valide (rend permanentes) les modifications dans la base de données. Sans cette ligne, l'insertion ne serait pas enregistrée.
    #conn.close()   # Ferme la connexion au serveur de base de données, libérant ainsi les ressources.
   # print("produit ajouter avec succés !") # Affiche un message de succès à l'utilisateur.
    
 #def voir_produits(): # Définit une fonction nommée 'voir_produits'.
     #conn = get_connection() # Établit la connexion à la base de données.
     #cur = conn.cursor()     # Crée l'objet curseur nécessaire pour exécuter la requête.
     #cur.execute("SELECT * FROM produits")  # Exécute une requête SQL SELECT pour sélectionner toutes les colonnes ('*') de la table 'produits'.
     #produits = cur.fetchall()  # 'cur.fetchall()' : Récupère TOUS les résultats renvoyés par la requête SELECT et les stocke dans la variable 'produits' sous forme d'une liste de tuples.
     #conn.close()  # Ferme immédiatement la connexion à la base de données.
     #if not produits:  # Teste si la liste 'produits' est vide (c-à-d, si 'fetchall()' n'a rien trouvé).
        # print("Aucun produit trouvé.")  # Affiche un message si la base est vide.
      #else:   # Si la liste n'est pas vide (il y a des produits à afficher).
         #for p in produits:  # Boucle (itère) sur chaque élément (chaque ligne/produit) récupéré dans la liste 'produits'.
             # print(f"{p[0]}. {p[1]} - {p[2]} £ ({p[3]} en stock)")
              
     # Affiche les détails du produit. Les éléments d'une ligne sont accédés par leur index (p[0] est l'ID, p[1] est le Nom, p[2] est le Prix, p[3] est le Stock).
 
