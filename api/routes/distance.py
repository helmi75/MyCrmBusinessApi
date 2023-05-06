from flask import Blueprint, request, jsonify
from utils.distance_calculator import distance_between_addresses

distance_routes = Blueprint('distance_routes', __name__)

@distance_routes.route("/distance", methods=["POST"])

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
