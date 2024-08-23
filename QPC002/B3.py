from qiskit import QuantumCircuit


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:
    qc.cx(0, 1)
    qc.cx(1, 0)
    qc.cx(0, 1)
    return qc


from qiskit.quantum_info import Statevector

qc = solve()
test = QuantumCircuit(2)
test.initialize([1, 2, 3, 4], normalize=True)
test = test.compose(qc)
print(test.draw())
print(Statevector(test).data)
