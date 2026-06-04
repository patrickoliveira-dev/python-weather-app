from api import (
    buscar_coordenadas,
    buscar_clima,
    buscar_previsao
)

from historico import (
    salvar_consulta,
    mostrar_historico,
    limpar_historico,
    mostrar_estatisticas
)

from models.consulta_clima import ConsultaClima

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
    print("4 - Estatísticas")
    print("5 - Sair")

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

            if not dados_clima:

                continue

            consulta = ConsultaClima.from_api(
                cidade,
                dados_clima
            )

            consulta.exibir()

            dados_previsao = buscar_previsao(
                latitude,
                longitude
            )

            if dados_previsao:

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

        mostrar_estatisticas()

    elif opcao == "5":

        print("\nEncerrando programa...")
        break

    else:

        print("\nOpção inválida.")