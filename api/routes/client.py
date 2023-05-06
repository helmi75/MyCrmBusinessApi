from flask import Blueprint, request, jsonify
from models.client import Client
import sqlite3

client_routes = Blueprint('client_routes', __name__)

@client_routes.route('/ajout_client', methods=['POST'])
def ajout_client():
    # Récupérer les données soumises via la requête POST
    data = request.get_json()

    # Se connecter à la base de données SQLite
    conn = sqlite3.connect('clients.db')

    # Insérer le nouveau client dans la table "clients"
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO clients (nom, prenom, email)
                      VALUES (?, ?, ?)''', (data['nom'], data['prenom'], data['emai']))
    client_id = cursor.lastrowid

    # Enregistrer les changements et fermer la connexion
    conn.commit()
    conn.close()

    # Renvoyer une réponse indiquant que le client a été ajouté avec succès
    return f"Le client avec l'ID {client_id} a été ajouté avec succès"

@client_routes.route('/clients', methods=['GET'])
def afficher_clients():
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    conn.close()
    return jsonify(clients)

