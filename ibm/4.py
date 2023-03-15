'''
Primeiramente, define-se o número de bits que serão utilizados para gerar o número aleatório, nesse caso, 8 bits.
Em seguida, cria-se um circuito quântico com n qubits e n bits clássicos.
O próximo passo é aplicar a porta Hadamard em todos os qubits, que coloca os qubits em uma superposição de estados.
Depois disso, mede-se os qubits e obtém-se um resultado binário.
O resultado é convertido em um número inteiro, que é o número aleatório gerado.

exemplo de código que usa o Qiskit para gerar números aleatórios:
'''
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import circuit_drawer

# Define a quantidade de bits para gerar o número aleatório
num_bits = 8

# Cria o circuito quântico
qc = QuantumCircuit(num_bits, num_bits)

# Aplica uma porta Hadamard em todos os qubits
for i in range(num_bits):
    qc.h(i)

# Medição dos resultados
qc.measure(range(num_bits), range(num_bits))

# Simulação do circuito
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=3)
result = job.result()

# Obtém o resultado da simulação
counts = result.get_counts(qc)
binary = list(counts.keys())[0]

# Converte o resultado em um número inteiro
random_int = int(binary, 2)

print(f"O número aleatório gerado é: {random_int}")

# Plot dos resultados
circuit_drawer(qc, filename='4-circuit.png', output='mpl', style={'backgroundcolor': '#EEEEEE'})

'''
O processo de geração de número aleatório é baseado na teoria quântica e na aleatoriedade intrínseca dos processos quânticos.
A partir da aplicação da porta Hadamard em todos os qubits, os estados dos qubits são colocados em uma superposição,
o que significa que cada qubit possui a mesma probabilidade de estar no estado 0 ou 1.

Ao medir os qubits, os estados entram em colapso e é obtido um resultado binário.
Como os estados estão em superposição, a medida é aleatória e o resultado é um número aleatório.
'''