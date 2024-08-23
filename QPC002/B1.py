from qiskit import QuantumCircuit


def solve(theta: float) -> QuantumCircuit:
    qc = QuantumCircuit(1)
    # Write your code here:
    qc.rz(-2 * theta, 0)
    return qc


from qiskit.quantum_info import Statevector

theta = 3.14
qc = solve(theta)
# test = QuantumCircuit(1)
# test.initialize("11")
# test = test.compose(qc)
print(qc.draw())
print(Statevector(qc).data)
