import json
from models.consulta_clima import ConsultaClima

def salvar_consulta(consulta):

    nova_consulta = consulta.to_dict()

    historico = carregar_historico()
    
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

    historico = carregar_historico()
    
    if historico is None:
        return

    if not historico:

        print("\nNenhum histórico encontrado.")
        return
    
    print("\n=== HISTÓRICO ===")

    for dados in historico:

        consulta = ConsultaClima.from_dict(
            dados
        )

        consulta.exibir()

def limpar_historico():

    with open(
        "historico.json",
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            [],
            arquivo,
            indent=4,
            ensure_ascii=False
        )
    
    print("\n🗑️ Histórico apagado com sucesso.")

def mostrar_estatisticas():

    historico = carregar_historico()

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

def carregar_historico():

    try:

        with open(
            "historico.json",
            "r",
            encoding="utf-8"
        ) as arquivo:
                
            return json.load(arquivo)
        
    except FileNotFoundError:

        return []
        
    except json.JSONDecodeError:

        print(
            "\n❌ Histórico corrompido."
        )

        return None