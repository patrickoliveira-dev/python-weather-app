import json
from models.consulta_clima import ConsultaClima

def salvar_consulta(consulta):

    nova_consulta = consulta.to_dict()

    try:

        with open(
            "historico.json",
            "r",
            encoding="utf-8"
        ) as arquivo:
            
            historico = json.load(arquivo)
    
    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        historico = []

    historico.append(nova_consulta)

    with open(
        "historico.json",
        "w",
        encoding="utf-8"
    ) as arquivo:
        
        json.dump(
            historico,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

def mostrar_historico():

    try:

        with open("historico.json", "r", encoding="utf-8") as arquivo:
            historico = json.load(arquivo)
    
    except FileNotFoundError:

        print("\nNenhum histórico encontrado.")
        return
    
    print("\n=== HISTÓRICO ===")

    """ for consulta in historico:

        print(f"\n📍 Cidade: {consulta['cidade']}")
        print(f"🕒 Data/Hora: {consulta['data_hora']}")
        print(f"🌡️ Temperatura: {consulta['temperatura']}°C")
        print(f"💨 Vento: {consulta['vento']} km/h") """
    
    for dados in historico:

        consulta = ConsultaClima.from_dict(
            dados
        )

        consulta.exibir()

def limpar_historico():

    with open("historico.json", "w", encoding="utf-8") as arquivo:

        json.dump(
            [],
            arquivo,
            indent=4,
            ensure_ascii=False
        )
    
    print("\n🗑️ Histórico apagado com sucesso.")

def mostrar_estatisticas():

    with open(
        "historico.json",
        "r",
        encoding="utf-8"
    ) as arquivo:
        
        historico = json.load(arquivo)

    if not historico:

        print("\nNenhuma consulta encontrada")
        return
    
    total = len(historico)

    temperaturas = [
        consulta["temperatura"]
        for consulta in historico
    ]

    media = sum(temperaturas) / len(temperaturas)

    maxima = max(temperaturas)

    minima = min(temperaturas)

    contagem_cidades = {}

    for consulta in historico:

        cidade = consulta["cidade"]

        if cidade not in contagem_cidades:

            contagem_cidades[cidade] = 0
        
        contagem_cidades[cidade] += 1
    
    cidade_mais_consultada = max(
        contagem_cidades,
        key=contagem_cidades.get
    )

    print("\n=== ESTATíSTICAS ===")

    print(f"📊 Total de consultas: {total}")

    print(
        f"🏙️ Cidade mais consultada: "
        f"{cidade_mais_consultada}"
    )

    print(
        f"🌡️ Temperatura média: "
        f"{media:.1f}°C"
    )

    print(
    f"🔥 Maior temperatura: "
    f"{maxima:.1f}°C"
    )

    print(
        f"🧊 Menor temperatura: "
        f"{minima:.1f}°C"
    )