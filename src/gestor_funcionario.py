from src.funcionario import Funcionario
from src.exceptions import *
from src.decorators import auditar_operacao


class GestorFuncionarios:
    _funcionarios:list[Funcionario] = None

    def __init__(self, funcionarios: list[Funcionario]):
        self.funcionarios = funcionarios

    def __repr__(self) -> str:
        return f'GestorFuncionarios(funcionarios={self.funcionarios!r})'

    @property
    def funcionarios(self):
        return self._funcionarios
    
    @funcionarios.setter
    def funcionarios(self, new):
        match new:
            case [*_] if all(isinstance(f,Funcionario) for f in new):
                self._funcionarios = new
            case _:
                raise ListaDeFuncionariosInvalida(
                    f"Valor inválido para 'funcionarios': {new}. É esperado uma list[Funcionario]."
                )
    
    @auditar_operacao
    def adicionar_funcionario(self, funcionario: Funcionario) -> None:
        self.funcionarios += [funcionario]
    
    @auditar_operacao
    def remover_funcionario(self, nome: str) -> None:
        [self.funcionarios.remove(f) for f in self.funcionarios if nome.lower() == f.nome.lower()]

    @auditar_operacao
    def buscar_funcionario(self, nome: str) -> list[Funcionario]:
        return [func for func in self.funcionarios if nome.lower() in func.nome.lower()]
    
    def gerar_relatorio(self) -> None:
       offset = 15
       print('\n\nRelatório: \n')
       [print(f' - Nome: {f.nome.ljust(offset)} | Cargo: {f.cargo.ljust(offset)} | Salário Final: R$ {f'{f.calcular_salario():.2f}'.ljust(offset)}') for f in self.funcionarios]
