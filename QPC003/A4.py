from qiskit import QuantumCircuit
import math


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    a = (1 / n) ** 0.5
    qc.ry(2 * math.acos(a), 0)
    for i in range(n - 2):
        a = (1 / (n - 1 - i)) ** 0.5
        qc.cry(2 * math.acos(a), i, i + 1)
    for i in range(1, n - 1)[::-1]:
        for j in range(i):
            qc.cx(i, j)
    qc.x(n - 1)
    for i in range(n - 1):
        qc.cx(i, n - 1)
    return qc


from qiskit.quantum_info import Statevector

qc = solve(3)
# test = QuantumCircuit(1)
# test.initialize("11")
# test = test.compose(qc)
print(qc.draw())
print(Statevector(qc).data)
