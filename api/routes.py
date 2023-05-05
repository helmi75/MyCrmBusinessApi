from flask import Blueprint, request, jsonify
from utils.distance_calculator import distance_between_addresses
from models.client import Client
import sqlite3

routes = Blueprint('routes', __name__)

@routes.route("/distance", methods=["POST"])
def calculate_distance():
    data = request.get_json()
    address1 = data.get("address1")
    address2 = data.get("address2")
    api_key = data.get("api_key")

    if not address1 or not address2 or not api_key:
        return jsonify({"error": "Les deux adresses et la clé API sont requises"}), 400

    distance = distance_between_addresses(address1, address2, api_key)

    if distance is not None:
        return jsonify({"distance_km": distance})
    else:
        return jsonify({"error": "Impossible de calculer la distance"}), 500

@routes.route('/ajout_client', methods=['POST'])
def ajout_client():
    # Récupérer les données soumises via la requête POST
    data = request.get_json()

    # Se connecter à la base de données SQLite
    conn = sqlite3.connect('clients.db')

    # Insérer le nouveau client dans la table "clients"
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO clients (nom, prenom, email)
                      VALUES (?, ?, ?)''', (data['nom'], data['prenom'], data['email']))
    client_id = cursor.lastrowid

    # Enregistrer les changements et fermer la connexion
    conn.commit()
    conn.close()

    # Renvoyer une réponse indiquant que le client a été ajouté avec succès
    return f"Le client avec l'ID {client_id} a été ajouté avec succès"

@routes.route('/clients', methods=['GET'])
def afficher_clients():
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    conn.close()
    return jsonify(clients)

