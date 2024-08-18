from qiskit import QuantumCircuit


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    qc.h(1)
    qc.ch(1, 0)
    qc.cx(0, 1)
    return qc


from qiskit.quantum_info import Statevector, Operator

qc = solve()
print(qc.draw())
print(Statevector(qc).data)
