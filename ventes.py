# ventes.py
from database import get_connection
from produits import voir_produits

def passer_commande():
    produits = voir_produits()
    if not produits:
        return

    try:
        produit_id = int(input("ID du produit : "))
        quantite = int(input("Quantité : "))
        if quantite <= 0:
            print("❌ La quantité doit être supérieure à 0.")
            return
    except ValueError:
        print("❌ Veuillez entrer des nombres valides.")
        return

    conn = get_connection()
    if not conn:
        return
    cur = conn.cursor()
    try:
        # Vérifier que le produit existe et récupérer prix et stock
        cur.execute("SELECT prix, stock FROM produits WHERE id = %s", (produit_id,))
        resultat = cur.fetchone()
        if not resultat:
            print("❌ Produit introuvable.")
            return

        prix, stock = resultat
        if quantite > stock:
            print("❌ Stock insuffisant.")
            return

        # Calcul du total et insertion de la vente
        total = prix * quantite
        cur.execute(
            "INSERT INTO ventes (produit_id, quantite, total) VALUES (%s, %s, %s)",
            (produit_id, quantite, total)
        )
        cur.execute(
            "UPDATE produits SET stock = stock - %s WHERE id = %s",
            (quantite, produit_id)
        )
        conn.commit()
        print(f"✅ Vente enregistrée : {quantite} x produit {produit_id} = {total:.2f} €")
    except Exception as e:
        print("⚠️ Une erreur est survenue :", e)
    finally:
        cur.close()
        conn.close()

def voir_ventes():
    """
    Affiche l'historique des ventes avec produit, quantité, total et date.
    """
    conn = get_connection()
    if not conn:
        return
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT v.id, p.nom, v.quantite, v.total, v.date_vente
            FROM ventes v
            JOIN produits p ON v.produit_id = p.id
            ORDER BY v.date_vente DESC
        """)
        ventes = cur.fetchall()
        if not ventes:
            print("⚠️ Aucune vente enregistrée.")
            return

        print("\n--- Historique des ventes ---")
        for v in ventes:
            print(f"{v[0]} - {v[1]} : {v[2]} unités = {v[3]:.2f} € ({v[4]})")
    except Exception as e:
        print("⚠️ Une erreur est survenue :", e)
    finally:
        cur.close()
        conn.close()


# from database import get_connection
# from produits import voir_produits
#
# def passer_commande():
#     conn = get_connection()
#     cur = conn.cursor()
#     voir_produits()
#     produit_id = int(input("ID du produit à acheter : "))
#     qte = int(input("Quantité : "))
#
#     cur.execute("SELECT prix, stock FROM produits WHERE id = %s", (produit_id,))
#     resultat = cur.fetchone()
#     if resultat:
#         prix, stock = resultat
#         if qte <= stock:
#             total = prix * qte
#             cur.execute("INSERT INTO ventes (produit_id, quantite, total) VALUES (%s, %s, %s)",
#                         (produit_id, qte, total))
#             cur.execute("UPDATE produits SET stock = stock - %s WHERE id = %s", (qte, produit_id))
#             conn.commit()
#             print(f"✅ Vente enregistrée ({qte} x produit {produit_id}) = {total} €")
#         else:
#             print("❌ Stock insuffisant.")
#     else:
#         print("❌ Produit non trouvé.")
#     conn.close()
#
# def voir_ventes():
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("""
#         SELECT v.id, p.nom, v.quantite, v.total, v.date_vente
#         FROM ventes v
#         JOIN produits p ON v.produit_id = p.id
#         ORDER BY v.date_vente DESC
#     """)
#     ventes = cur.fetchall()
#     conn.close()
#     for v in ventes:
#         print(f"{v[0]} - {v[1]} : {v[2]} unités = {v[3]} € ({v[4]})")

