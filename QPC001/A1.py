from qiskit import QuantumCircuit
from qiskit.circuit.library import HGate


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(1)
    hgate = HGate()
    qc.append(hgate, [0])
    return qc


from qiskit.quantum_info import Statevector

qc = solve()
print(qc.data)
print(qc.draw())
print(Statevector(qc).data)
