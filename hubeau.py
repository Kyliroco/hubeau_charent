import requests

# Construction de l'URL de l'API
url = f"https://hubeau.eaufrance.fr/api/v1/ecoulement/stations?format=json&code_departement=17"

# Envoie de la requête GET à l'API
response = requests.get(url)

# Vérification du succès de la requête
if response.status_code == 206 or response.status_code == 200:
    data = response.json()
    # On récuper le code de toutes les stations et on le met dans une liste 
    stations = [station['code_station'] for station in data['data']]
    ecoulements = []    
    for station in stations:
        # Construction de l'URL de l'API
        url = f"https://hubeau.eaufrance.fr/api/v1/ecoulement/observations?format=json&code_station={station}"
        # Envoie de la requête GET à l'API
        response = requests.get(url)
        # Vérification du succès de la requête
        if response.status_code == 206 or response.status_code == 200:
            ecoulements.append(response.json())
        else:
            print(f"Erreur lors de la récupération des données : {response.status_code}")
    # Affiche les données récupérées
    # print(data)
else:
    print(f"Erreur lors de la récupération des données : {response.status_code}")

print(ecoulements)
