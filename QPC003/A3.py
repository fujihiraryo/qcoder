from qiskit import QuantumCircuit
import math


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(3)
    # Write your code here:
    a = (1 / 3) ** 0.5
    qc.ry(2 * math.acos(a), 0)
    qc.ch(0, 1)
    qc.x(2)
    qc.cx(0, 2)
    qc.cx(1, 0)
    return qc


from qiskit.quantum_info import Statevector

qc = solve()
# test = QuantumCircuit(1)
# test.initialize("11")
# test = test.compose(qc)
print(qc.draw())
print(Statevector(qc).data)
