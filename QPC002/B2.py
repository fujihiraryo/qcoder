from qiskit import QuantumCircuit
from qiskit.circuit.library import PhaseGate


def solve(n: int, L: int, theta: float) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    for i in range(n):
        if not ((L >> i) & 1):
            qc.x(i)
    if n == 1:
        qc.append(PhaseGate(theta), [0])
    else:
        qc.append(PhaseGate(theta).control(n - 1), range(n))
    for i in range(n):
        if not ((L >> i) & 1):
            qc.x(i)
    return qc


from qiskit.quantum_info import Statevector

n = 1
L = 0
theta = 3.1415
qc = solve(n, L, theta)
test = QuantumCircuit(n)
for i in range(n):
    test.h(i)
test = test.compose(qc)
print(test.draw())
print(Statevector(test).data)
