from qiskit import QuantumCircuit


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    qc.h(range(n // 2))
    for i in range(n // 2, n):
        qc.cx(0, i)
    return qc


from qiskit.quantum_info import Statevector

n = 4
qc = solve(n)
# test = QuantumCircuit(1)
# test.initialize("11")
# test = test.compose(qc)
print(qc.draw())
print(Statevector(qc).data)
