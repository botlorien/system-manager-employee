from dataclasses import dataclass

from src.funcionario import Funcionario


@dataclass(frozen=True)
class Gerente(Funcionario):
    cargo: str = 'Gerente'

    def calcular_salario(self):
        return 1.2 * self.salario_base
    
if __name__=='__main__':
    g = Gerente(
        'Ben-Hur',
        10000.0
    )
    print(g)
    print(g.calcular_salario())