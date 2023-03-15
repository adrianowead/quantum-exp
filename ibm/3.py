'''
exemplo bem simples e documentado de como implementar um algoritmo genético usando qubits na biblioteca Qiskit
'''

# Importando as bibliotecas necessárias
from qiskit import QuantumCircuit, Aer, execute
import numpy as np

# Define o tamanho da população e o número de genes em cada indivíduo
tam_populacao = 5
num_genes = 2

# Cria uma população aleatória de indivíduos
populacao = np.random.randint(0, 2, size=(tam_populacao, num_genes))

# Define o número de gerações
num_geracoes = 10

# Define o número de qubits necessários para codificar cada gene
num_qubits = 1

# Define a função de aptidão
def aptidao(individuo):
    # Converte o indivíduo de binário para decimal
    valor_decimal = int(''.join(map(str, individuo)), 2)
    # Calcula a função fitness (f(x) = x^2)
    return valor_decimal**2

# Cria um circuito quântico com um qubit para cada gene
circuito = QuantumCircuit(num_genes * num_qubits, num_genes)

# Adiciona as portas X para os genes de indivíduos selecionados aleatoriamente
for i in range(tam_populacao):
    if np.random.rand() < 0.5:
        circuito.x(range(num_genes * num_qubits))

# Adiciona a porta Hadamard a todos os qubits para criar superposições
circuito.h(range(num_genes * num_qubits))

# Adiciona a porta de medição em todos os qubits
circuito.measure(range(num_genes * num_qubits), range(num_genes))

# Configura o simulador de backend do Qiskit para executar o circuito
backend = Aer.get_backend('qasm_simulator')

# Executa o circuito em cada indivíduo na população e calcula o fitness
fitness = []
for i in range(tam_populacao):
    # Codifica os genes do indivíduo em qubits
    for j in range(num_genes):
        if populacao[i][j] == 1:
            circuito.x(j * num_qubits)
    # Executa o circuito no simulador de backend e mede os resultados
    resultado = execute(circuito, backend).result()
    contagem = resultado.get_counts(circuito)
    # Calcula o fitness do indivíduo
    fit = 0
    for k, v in contagem.items():
        fit += aptidao(list(map(int, k[::-1]))) * v
    fitness.append(fit)

# Imprime a população inicial e o fitness
print("População inicial:")
print(populacao)
print("Fitness inicial:")
print(fitness)

# Loop principal do algoritmo genético
for i in range(num_geracoes):
    # Seleciona dois indivíduos aleatoriamente
    indices = np.random.choice(range(tam_populacao), size=2, replace=False)
    individuo1 = populacao[indices[0]]
    individuo2 = populacao[indices[1]]
    
    # Realiza o crossover para criar dois novos indivíduos
    ponto_corte = np.random.randint(num_genes)
    filho1 = np.concatenate((individuo1[:ponto_corte], individuo2[ponto_corte:]))
    filho2 = np.concatenate
