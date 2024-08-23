from qiskit import QuantumCircuit


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(1)
    # Write your code here:
    qc.x(0)
    qc.z(0)
    qc.x(0)
    return qc


from qiskit.quantum_info import Statevector

qc = solve()
# test = QuantumCircuit(1)
# test.initialize("11")
# test = test.compose(qc)
print(qc.draw())
print(Statevector(qc).data)
