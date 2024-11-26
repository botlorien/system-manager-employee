from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class Funcionario(ABC):
    nome: str
    salario_base: float

    @abstractmethod
    def calcular_salario(self) -> float:
        """Classe abstrata para ser implementada pelas subclasses"""
        pass

if __name__=='__main__':
    ...