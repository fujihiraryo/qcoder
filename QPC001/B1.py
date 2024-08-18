from qiskit import QuantumCircuit, QuantumRegister


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # qc.cx(0, 1)
    qc.initialize("01", qc.qubits)
    return qc


from qiskit.quantum_info import Statevector

qc = solve()
print(qc.draw())
print(Statevector(qc).data)
