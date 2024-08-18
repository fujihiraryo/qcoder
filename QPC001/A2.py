from qiskit import QuantumCircuit
from qiskit.circuit.library import HGate


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    for i in range(n):
        sub = QuantumCircuit(1)
        sub.h(0)
        qc.compose(sub, [i], inplace=True)
    return qc


from qiskit.quantum_info import Statevector

qc = solve(3)
print(qc.data)
print(qc.draw())
print(Statevector(qc).data)
