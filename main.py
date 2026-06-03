from api import (
    buscar_coordenadas,
    buscar_clima,
    buscar_previsao
)

from historico import (
    salvar_consulta,
    mostrar_historico,
    limpar_historico
)

from models.consulta_clima import ConsultaClima

""" def mostrar_clima(dados):

    temperatura = dados["current"]["temperature_2m"]
    vento = dados["current"]["wind_speed_10m"]

    print("\n=== CLIMA ATUAL ===")
    print(f"🌡️ Temperatura: {temperatura}°C")
    print(f"💨 Vento: {vento} km/h") """

def mostrar_previsao(dados):
    datas = dados["daily"]["time"]

    temperaturas_max = dados["daily"]["temperature_2m_max"]

    temperaturas_min = dados["daily"]["temperature_2m_min"]

    print("\n=== PREVISÃO DOS PRÓXIMOS DIAS ===")

    for data, temp_max, temp_min in zip(
        datas,
        temperaturas_max,
        temperaturas_min
    ):
        print(f"\n📅 {data}")
        print(f"⬆️ Máxima: {temp_max}°C")
        print(f"⬇️ Mínima: {temp_min}°C")

while True:

    print("\n=== WEATHER APP ===")
    print("1 - Consultar cidade")
    print("2 - Ver histórico")
    print("3 - Limpar histórico")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        cidade = input("\nDigite uma cidade: ")

        coordenadas = buscar_coordenadas(cidade)

        if coordenadas:

            latitude, longitude = coordenadas

            dados_clima = buscar_clima(
                latitude,
                longitude
            )

            temperatura = dados_clima["current"]["temperature_2m"]
            vento = dados_clima["current"]["wind_speed_10m"]

            consulta = ConsultaClima(
                cidade,
                temperatura,
                vento
            )

            consulta.exibir()

            dados_previsao = buscar_previsao(
                latitude,
                longitude
            )

            mostrar_previsao(dados_previsao)

            salvar_consulta(consulta)

    elif opcao == "2":

        mostrar_historico()
    
    elif opcao == "3":

        confirmar = input(
            "\nTem certeza? (s/n): "
        ).lower()

        if confirmar == "s":

            limpar_historico()
    
    elif opcao == "4":

        print("\nEncerrando programa...")
        break

    else:

        print("\nOpção inválida.")