from qiskit import QuantumCircuit, QuantumRegister


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n + 1)
    for i in range(n):
        qc.cx(i, n)
    return qc


from qiskit.quantum_info import Statevector, Operator

qc = solve(3)
print(qc.draw())
print(Statevector(qc).data)
