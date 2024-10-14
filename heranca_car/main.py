from heranca_car.carro import Carro
from heranca_car.carro_eletrico import carroEletrico


meuCarro = Carro("Ford", "Fusion", 2021)
meuCarroEletrico = carroEletrico("Toyota", "Modelo Special", 2022)
print(meuCarroEletrico.geraNomeCarro())
meuCarroEletrico.descricaoBateria()