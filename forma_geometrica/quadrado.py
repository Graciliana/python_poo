class Quadrado:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        area = self.base * self.altura 
        return area

    def calcularPerimetro(self):
        perimetro = self.base + 2 * (self.altura**2 + (self.base / 2) ** 2) ** 0.5
        return perimetro

        # Método para imprimir a área e comprimentos

    def imprimir_detalhes(self):
        area = self.calcularArea()
        perimetro = self.calcularPerimetro()
        print(
            f"Base: {self.base}, Altura: {self.altura}, Área: {area}, Perímetro: {perimetro}"
        )
