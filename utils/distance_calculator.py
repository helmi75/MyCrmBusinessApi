import requests
def get_coordinates(address):
    api_url = "https://api-adresse.data.gouv.fr/search/"
    params = {
        'q': address
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['features']:
            coordinates = data['features'][0]['geometry']['coordinates']
            return coordinates[::-1]  # Invert the order to (latitude, longitude)
    return None


def distance_between_addresses(address1, address2, api_key):
    """  
	corriger la  valeur du retourd 'api  
    """
    coordinates1 = get_coordinates(address1)[::-1]
    coordinates2 = get_coordinates(address2)[::-1]

    if not coordinates1 or not coordinates2:
        return None

    api_url = "https://api.openrouteservice.org/v2/matrix/driving-car"
    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        'Authorization': api_key,
        'Content-Type': 'application/json; charset=utf-8'
    }
    body = {"locations":[coordinates1, coordinates2],
            "metrics":["distance"],
            "units":"km"
           }

    response = requests.post(api_url, headers=headers, json=body)
    
    if response.status_code == 200:
        data = response.json()
        distance_meters = data["distances"][0][1] 
        distance_kilometers = distance_meters 
        return distance_kilometers
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
