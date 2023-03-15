'''
Aqui está um exemplo de código Python
usando o pacote Qiskit da IBM para criar e executar um circuito quântico simples de duas portas.
'''

# Importa as classes e funções necessárias do Qiskit
from qiskit import QuantumCircuit, execute, Aer, QuantumRegister, ClassicalRegister

# Cria um circuito quântico com 2 qubits e 2 bits clássicos
circuito = QuantumCircuit(QuantumRegister(2), ClassicalRegister(2))

# Adiciona uma porta Hadamard no primeiro qubit (qubit 0)
circuito.h(0)

# Adiciona uma porta CX (CNOT) no segundo qubit (qubit 1) controlado pelo primeiro qubit (qubit 0)
circuito.cx(0, 1)

# Mede os dois qubits e armazena os resultados nos bits clássicos correspondentes
circuito.measure([0,1], [0,1])

# Configura o simulador de backend do Qiskit para executar o circuito
backend = Aer.get_backend('qasm_simulator')

# Executa o circuito no simulador de backend e imprime os resultados
resultado = execute(circuito, backend).result()
print(resultado.get_counts(circuito))

'''
Este código cria um circuito quântico simples que aplica uma porta Hadamard a um qubit e uma porta CX (CNOT) a outro qubit controlado pelo primeiro.
Em seguida, mede os dois qubits e imprime os resultados. 

Este exemplo usa o simulador de backend do Qiskit para executar o circuito, mas você também pode usar um computador quântico real da IBM se tiver acesso a ele.
'''
