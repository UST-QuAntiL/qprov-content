from qiskit import QuantumCircuit

qc = QuantumCircuit(4,2)

# initialize a=1, b=1, carry=1
qc.x(0)
qc.x(1)
qc.x(2)

qc.barrier()
qc.ccx(0,1,3)
qc.cx(0,1)
qc.ccx(1,2,3)
qc.cx(1,2)
qc.cx(0,1)
qc.barrier()

# extract outputs
qc.measure(2,0)
qc.measure(3,1)

qc.draw(output='mpl', filename='adder-initialized.png')
