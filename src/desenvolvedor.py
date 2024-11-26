from dataclasses import dataclass

from src.funcionario import Funcionario


@dataclass(frozen=True)
class Desenvolvedor(Funcionario):
    cargo: str = 'Desenvolvedor'

    def calcular_salario(self) -> float:
        return 1.1 * self.salario_base

if __name__=='__main__':
    dev = Desenvolvedor(
        "Ben-Hur",
        7000.00

    )
    print(dev)
    print(dev.calcular_salario())
