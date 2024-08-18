from qiskit import QuantumCircuit


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    qc.cx(0, 1)
    return qc


from qiskit.quantum_info import Statevector

qc = solve()
test = QuantumCircuit(2)
test.initialize("11")
test = test.compose(qc)
print(qc.draw())
print(test.draw())
print(Statevector(test).data)
