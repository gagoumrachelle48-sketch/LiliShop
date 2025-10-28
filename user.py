# users.py
from database import get_connection
import mysql.connector
import hashlib

def hash_password(password):
    """Hash le mot de passe avec SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    """Authentifie un utilisateur et retourne ses informations si correct."""
    print("\n=== Connexion utilisateur ===")
    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")
    password_hash = hash_password(password)

    conn = get_connection()
    if not conn:
        print("❌ Impossible de se connecter à la base de données.")
        return None

    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT id, role FROM users WHERE username=%s AND password=%s",
            (username, password_hash)
        )
        user = cur.fetchone()
        if user:
            print(f"✅ Connexion réussie ! Bienvenue {username} ({user[1]})")
            return {"id": user[0], "username": username, "role": user[1]}
        else:
            print("❌ Identifiants incorrects.")
            return None
    except mysql.connector.Error as err:
        print("⚠️ Erreur MySQL :", err)
        return None
    finally:
        cur.close()
        conn.close()

def create_user():
    """Crée un nouvel utilisateur dans la base de données."""
    print("\n=== Création d'un nouvel utilisateur ===")
    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")
    role = input("Rôle (admin/employe) : ").lower()

    if role not in ["admin", "employe"]:
        print("❌ Rôle invalide. Choisir 'admin' ou 'employe'.")
        return

    conn = get_connection()
    if not conn:
        print("❌ Impossible de se connecter à la base de données.")
        return

    cur = conn.cursor()
    try:
        # Vérifier si le nom d'utilisateur existe déjà
        cur.execute("SELECT id FROM users WHERE username=%s", (username,))
        if cur.fetchone():
            print("❌ Ce nom d'utilisateur existe déjà.")
            return

        # Hash du mot de passe avant insertion
        password_hash = hash_password(password)

        # Insérer l'utilisateur
        cur.execute(
            "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
            (username, password_hash, role)
        )
        conn.commit()
        print("✅ Utilisateur créé avec succès !")
    except mysql.connector.Error as err:
        print("⚠️ Erreur MySQL :", err)
    finally:
        cur.close()
        conn.close()
