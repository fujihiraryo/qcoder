from qiskit import QuantumCircuit


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:
    qc.h(0)
    qc.cx(0, 1)
    # qc.cz(0, 1)
    # qc.x(1)
    # qc.z(0)
    return qc


from qiskit.quantum_info import Statevector

qc = solve()
# test = QuantumCircuit(1)
# test.initialize("11")
# test = test.compose(qc)
print(qc.draw())
print(Statevector(qc).data)
