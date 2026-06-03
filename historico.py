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