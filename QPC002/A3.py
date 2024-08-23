from qiskit import QuantumCircuit


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    qc.h(0)
    for i in range(1, n):
        qc.cx(0, i)
    qc.cz(0, 1)
    return qc


from qiskit.quantum_info import Statevector

n = 2
qc = solve(n)
# test = QuantumCircuit(1)
# test.initialize("11")
# test = test.compose(qc)
print(qc.draw())
print(Statevector(qc).data)
