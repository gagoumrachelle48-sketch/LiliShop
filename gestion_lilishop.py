# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector
#
# # Connexion à MySQL
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Mabellerachou@93",
#     database="LiliShop"
# )
# cursor = conn.cursor()
#
# # Fonction appelée par le bouton
# def ajouter_produit_gui():
#     nom = entry_nom.get()
#     prix = float(entry_prix.get())
#     stock = int(entry_stock.get())
#     ajouter_produit(nom, prix, stock)
#     messagebox.showinfo("Succès", f"Produit '{nom}' ajouté avec succès !")
#
# # Fonction console (déjà existante)
# def ajouter_produit(nom, prix, stock):
#     cursor.execute("INSERT INTO produits (nom, prix, stock) VALUES (%s, %s, %s)", (nom, prix, stock))
#     conn.commit()
#
# # Interface graphique
# fenetre = tk.Tk()
# fenetre.title("Ajouter un produit - LiliShop")
#
# tk.Label(fenetre, text="Nom du produit").grid(row=0, column=0)
# entry_nom = tk.Entry(fenetre)
# entry_nom.grid(row=0, column=1)
#
# tk.Label(fenetre, text="Prix").grid(row=1, column=0)
# entry_prix = tk.Entry(fenetre)
# entry_prix.grid(row=1, column=1)
#
# tk.Label(fenetre, text="Stock").grid(row=2, column=0)
# entry_stock