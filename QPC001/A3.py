from qiskit import QuantumCircuit


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    qc.h(1)
    qc.cx(1, 0)
    return qc


from qiskit.quantum_info import Statevector, Operator

qc = solve()
print(qc.draw())
print(Statevector(qc).data)
print(Operator(qc).data)
