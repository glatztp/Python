class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano}"

class Moto(Veiculo):
        def __init__(self, marca, modelo, ano):
            super().__init__(marca, modelo, ano)

        def __str__(self):
            return (f"M: {super().__str__()}")

class Carro(Veiculo):
      def __init__(self, marca, modelo, ano):
          super().__init__(marca, modelo, ano)

      def __str__(self):
          return (f"C: {super().__str__()}")


carro = Carro("honda", "civic", "2020")
moto = Moto("honda", "cj 170 start", "2023")

print(carro)
print(moto)
  