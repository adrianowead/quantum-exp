'''
exemplo que utiliza as quatro operações básicas da computação quântica: porta X, porta Y, porta Z e porta Hadamard
'''

# Importa as classes e funções necessárias do Qiskit
from qiskit import QuantumCircuit, execute, Aer

# Cria um circuito quântico com 1 qubit e 1 bit clássico
circuito = QuantumCircuit(1, 1)

# Adiciona uma porta X (NOT) ao qubit
circuito.x(0)

# Adiciona uma porta Y ao qubit
circuito.y(0)

# Adiciona uma porta Z ao qubit
circuito.z(0)

# Adiciona uma porta Hadamard ao qubit
circuito.h(0)

# Mede o qubit e armazena o resultado no bit clássico correspondente
circuito.measure(0, 0)

# Configura o simulador de backend do Qiskit para executar o circuito
backend = Aer.get_backend('qasm_simulator')

# Executa o circuito no simulador de backend e imprime os resultados
resultado = execute(circuito, backend).result()
print(resultado.get_counts(circuito))

'''
Este exemplo cria um circuito quântico com um único qubit e um único bit clássico.
Em seguida, aplica uma porta X (NOT) ao qubit, seguida por portas Y, Z e Hadamard.
O circuito mede o qubit e armazena o resultado no bit clássico correspondente.
Este exemplo também usa o simulador de backend do Qiskit para executar o circuito e imprime os resultados.
'''