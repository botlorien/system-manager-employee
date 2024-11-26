from src.desenvolvedor import Desenvolvedor
from src.gerente import Gerente
from src.gestor_funcionario import GestorFuncionarios

# Instanciando gestor
gestor = GestorFuncionarios([
    Desenvolvedor(nome='João Pedro',salario_base=6500),
    Gerente(nome='Ben-Hur Santos',salario_base=11000)
])

# Exibindo representação do gestor
print(gestor,'\n\n')

# Adicionando novos funcionarios
gestor.adicionar_funcionario(
    Desenvolvedor(nome='Maria Luiza',salario_base=6800)
)
gestor.adicionar_funcionario(
    Desenvolvedor(nome='Alvaro Cruz',salario_base=5200)
)

# Removendo um funcionario
gestor.remover_funcionario('joão pedro')

# Buscando Funcionarios
print(f"Funcionarios encontrados: \n{gestor.buscar_funcionario('Alvaro')}")

# Gerando relatorio
gestor.gerar_relatorio()