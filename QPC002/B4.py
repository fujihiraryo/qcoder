from qiskit import QuantumCircuit
from qiskit.circuit.library import PhaseGate
import numpy as np


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    if n == 1:
        qc.h(0)
        return qc
    for i in range(n):
        qc.h(i)
        for k in range(i + 1, n):
            qc.append(PhaseGate(np.pi / (2 ** (k - i))).control(1), [k, i])
    qc.swap(0, n - 1)
    for i in range(n // 2):
        qc.swap(i, n - i - 1)
    return qc


from qiskit.quantum_info import Statevector

n = 4
qc = solve(n)
test = QuantumCircuit(n)
test.initialize("1110")
# test.h(range(n))
test = test.compose(qc)
print(test.draw())
print(Statevector(test).data)
