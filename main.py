# main.py
from user import login, create_user
from produits import ajouter_produit, voir_produits
from ventes import passer_commande, voir_ventes

def menu(user):
    while True:
        print("\n===== MENU LILISHOP =====")
        print("1. Ajouter un produit (admin)")
        print("2. Voir les produits")
        print("3. Passer une commande")
        print("4. Voir les ventes")
        print("5. Créer un utilisateur (admin)")
        print("6. Quitter")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            if user.get("role") == "admin":
                ajouter_produit()
            else:
                print("⛔ Accès réservé à l’administrateur.")
        elif choix == "2":
            voir_produits()
        elif choix == "3":
            passer_commande()
        elif choix == "4":
            voir_ventes()
        elif choix == "5":
            if user.get("role") == "admin":
                create_user()
            else:
                print("⛔ Accès réservé à l’administrateur.")
        elif choix == "6":
            print("👋 Déconnexion. À bientôt !")
            break
        else:
            print("❌ Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    print("=== Bienvenue sur LiliShop ===")
    utilisateur = login()
    if utilisateur:
        menu(utilisateur)
    else:
        print("❌ Échec de la connexion. Veuillez vérifier vos identifiants et réessayer.")


        
# from users import login, create_user
# from produits import ajouter_produit, voir_produits
# from ventes import passer_commande, voir_ventes
#
# def menu(user):
#     while True:
#         print("\n===== MENU TECHSHOP MYSQL =====")
#         print("1. Ajouter un produit (admin seulement)")
#         print("2. Voir les produits")
#         print("3. Passer une commande")
#         print("4. Voir les ventes")
#         print("5. Créer un nouvel utilisateur (admin)")
#         print("6. Quitter")
#         choix = input("Votre choix : ")
#
#         if choix == "1":
#             if user["role"] == "admin":
#                 ajouter_produit()
#             else:
#                 print("⛔ Accès réservé à l’administrateur.")
#         elif choix == "2":
#             voir_produits()
#         elif choix == "3":
#             passer_commande()
#         elif choix == "4":
#             voir_ventes()
#         elif choix == "5":
#             if user["role"] == "admin":
#                 create_user()
#             else:
#                 print("⛔ Accès réservé à l’administrateur.")
#         elif choix == "6":
#             print("👋 Déconnexion.")
#             break
#         else:
#             print("❌ Choix invalide.")
#
# if __name__ == "__main__":
#     utilisateur = login()
#     if utilisateur:
#         menu(utilisateur)

