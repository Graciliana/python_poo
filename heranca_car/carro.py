class carro:
  def __init__(self, cor, modelo, ano):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.kilometragem = 0
    
  def geraNomeCarro(self):
    fullName = f"{self.marca} {self.modelo} {self.ano}"
    return fullName
  def getKilometragem(self):
   print(f"Esse carro ja rodou {self.kilometragem} kilometros.")
  
  def atualizaKilometragem(self, kilometros):
    if kilometros >= self.kilometragem:
      self.kilometragem = kilometros
    else:
      print("Nao pode resetar kilometragem")  
  def addKilometragem(self, kilometros):
    self.kilometragem = self.kilometragem + kilometros