from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
import math


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    a = (1 / 3) ** 0.5
    qc.ry(2 * math.acos(a), 0)
    qc.ch(0, 1)
    qc.cx(1, 0)
    return qc


from qiskit.quantum_info import Statevector, Operator

qc = solve()
print(qc.draw())
print(Statevector(qc).data)
