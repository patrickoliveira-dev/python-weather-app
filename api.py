import requests

def buscar_coordenadas(cidade):

    url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={cidade}"
        f"&count=1"
    )

    try:

        resposta = requests.get(
            url,
            timeout=10
        )

        resposta.raise_for_status()

        dados = resposta.json()
    
    except requests.exceptions.RequestException:

        print(
            "\n❌ Erro ao consultar a API de geolocalização."
        )

        return None

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

    try:

        resposta = requests.get(
            url,
            timeout=10
        )

        resposta.raise_for_status()

        return resposta.json()
    
    except requests.exceptions.RequestException:

        print(
            "\n❌ Erro ao consultar a API de clima."
        )

        return None

def buscar_previsao (latitude, longitude):

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&daily=temperature_2m_max,temperature_2m_min"
    )

    try:

        resposta = requests.get(
            url,
            timeout=10
        )

        resposta.raise_for_status()

        return resposta.json()
    
    except requests.exceptions.RequestException:

        print(
            "\n❌ Erro ao consultar a API de previsão."
        )

        return None