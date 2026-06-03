import requests

def buscar_coordenadas(cidade):

    url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={cidade}"
        f"&count=1"
    )

    resposta = requests.get(url)

    dados = resposta.json()

    if "results" not in dados:
        print("Cidade não encontrada.")
        return None

    resultado = dados["results"][0]

    latitude = resultado["latitude"]
    longitude = resultado["longitude"]

    return latitude, longitude

def buscar_clima(latitude, longitude):

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,wind_speed_10m"
    )

    resposta = requests.get(url)

    return resposta.json()

def buscar_previsao (latitude, longitude):

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&daily=temperature_2m_max,temperature_2m_min"
    )

    resposta = requests.get(url)

    return resposta.json()