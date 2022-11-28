import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


def printm(m):
    for i in m:
        print(" ".join(list(map(str,i))))

def converbi(num):
    cont = 0
    res = 0
    while cont < len(num):
        res += int(num[-1-cont])*(2**cont)
        cont += 1
    return res

simulator = Aer.get_backend('qasm_simulator')

print("Funcion 1")
print("0--->1")
print("1--->1")

mat1 = [[0 for k in range(4)] for l in range(4)]

cont = 0

for i in range(2):
    for j in range(2):
        circuit = QuantumCircuit(2, 2)
        if i == 1:
            circuit.x(0)
        if j == 1:
            circuit.x(1)
        circuit.barrier()
        circuit.x(1)
        circuit.barrier()
        circuit.measure([0,1],[1,0])
        circuit.barrier()

        compiled_circuit = transpile(circuit, simulator)

        job = simulator.run(compiled_circuit, shots=1000)

        result = job.result()

        counts = result.get_counts(circuit)

        for k in counts:
            mat1[converbi(k)][cont] = 1
        cont += 1
printm(mat1)


print("Funcion 2")
print("0--->0")
print("1--->1")

mat2 = [[0 for k in range(4)] for l in range(4)]

cont = 0

for i in range(2):
    for j in range(2):
        circuit = QuantumCircuit(2, 2)
        if i == 1:
            circuit.x(0)
        if j == 1:
            circuit.x(1)
        circuit.barrier()
        circuit.cnot(0,1)
        circuit.barrier()
        circuit.measure([0,1],[1,0])
        circuit.barrier()

        compiled_circuit = transpile(circuit, simulator)

        job = simulator.run(compiled_circuit, shots=1000)

        result = job.result()

        counts = result.get_counts(circuit)

        for k in counts:
            mat2[converbi(k)][cont] = 1
        cont += 1
printm(mat2)


print("Funcion 3")
print("0--->1")
print("1--->0")

mat3 = [[0 for k in range(4)] for l in range(4)]

cont = 0

for i in range(2):
    for j in range(2):
        circuit = QuantumCircuit(2, 2)
        if i == 1:
            circuit.x(0)
        if j == 1:
            circuit.x(1)
        circuit.barrier()
        circuit.x(0)
        circuit.cnot(0,1)
        circuit.x(0)
        circuit.barrier()
        circuit.measure([0,1],[1,0])
        circuit.barrier()

        compiled_circuit = transpile(circuit, simulator)

        job = simulator.run(compiled_circuit, shots=1000)

        result = job.result()

        counts = result.get_counts(circuit)

        for k in counts:
            mat3[converbi(k)][cont] = 1
        cont += 1
printm(mat3)

print("Funcion 4")
print("0--->0")
print("1--->0")

mat4 = [[0 for k in range(4)] for l in range(4)]

cont = 0

for i in range(2):
    for j in range(2):
        circuit = QuantumCircuit(2, 2)
        if i == 1:
            circuit.x(0)
        if j == 1:
            circuit.x(1)
        circuit.barrier()
        circuit.barrier()
        circuit.measure([0,1],[1,0])
        circuit.barrier()

        compiled_circuit = transpile(circuit, simulator)

        job = simulator.run(compiled_circuit, shots=1000)

        result = job.result()

        counts = result.get_counts(circuit)

        for k in counts:
            mat4[converbi(k)][cont] = 1
        cont += 1
printm(mat4)