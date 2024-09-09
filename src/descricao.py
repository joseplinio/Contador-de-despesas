from dataclasses import dataclass

@dataclass
class Descricao:
    data: str
    valor: float
    categoria: str

    def __str__(self):
        return f'Data: {self.data}, Valor: R${self.valor:.2f}, Categoria: {self.categoria}'