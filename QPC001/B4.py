from qiskit import QuantumCircuit
from qiskit.circuit.library import ZGate


def solve(n: int, L: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    for l in range(L):
        for i in range(n):
            # check if i-th bit of l is 0 or 1
            if not ((l >> i) & 1):
                qc.x(i)
        if n == 1:
            qc.z(0)
        else:
            # apply multiple controlled Z gate
            qc.append(ZGate().control(n - 1), range(n))
        for i in range(n):
            if not ((l >> i) & 1):
                qc.x(i)
    return qc


from qiskit.quantum_info import Statevector, Operator

qc = solve(3, 2)
print(qc.draw())
print(Statevector(qc).data)
