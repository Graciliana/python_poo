
from heranca_car.carro import Carro

class carroEletrico(Carro):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.amperagem_bateria = 75

    def descricaoBateria(self):
        print(f" Esse carro tem uma bateria de {self.amperagem_bateria} amperes")
