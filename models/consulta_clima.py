from datetime import datetime

class ConsultaClima:

    def __init__(
            self,
            cidade,
            temperatura,
            vento
    ):
        
        self.cidade = cidade
        self.temperatura = temperatura
        self.vento = vento

        self.data_hora = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

    def exibir(self):

        print(f"\n📍 Cidade: {self.cidade}")
        print(f"🕒 Data/Hora: {self.data_hora}")
        print(f"🌡️ Temperatura: {self.temperatura}°C")
        print(f"💨 Vento: {self.vento} km/h")

    def to_dict(self):

        return {
            "cidade": self.cidade,
            "temperatura": self.temperatura,
            "vento": self.vento,
            "data_hora": self.data_hora
        }
    
    @classmethod
    def from_dict(cls, dados):

        consulta = cls(
            dados["cidade"],
            dados["temperatura"],
            dados["vento"]
        )

        consulta.data_hora = dados["data_hora"]

        return consulta
    
    @classmethod
    def from_api(cls, cidade, dados):

        temperatura = dados["current"]["temperature_2m"]
        vento = dados["current"]["wind_speed_10m"]

        return cls(
            cidade,
            temperatura,
            vento
        )