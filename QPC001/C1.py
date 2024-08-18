from qiskit import QuantumCircuit


def solve(n: int, L: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)

    return qc


from qiskit.quantum_info import Statevector

qc = solve(3, 2)
print(qc.draw())
print(Statevector(qc).data)
