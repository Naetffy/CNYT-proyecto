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

##FUNCION CONSTANTE##

print("Funcion 1")
print("0000--->0")
print("0001--->0")
print("0010--->0")
print("0011--->0")
print("0100--->0")
print("0101--->0")
print("0110--->0")
print("0111--->0")
print("1000--->0")
print("1001--->0")
print("1010--->0")
print("1011--->0")
print("1100--->0")
print("1101--->0")
print("1110--->0")
print("1111--->0")

mat1 = [[0 for k in range(2**(5))] for l in range(2**(5))]

cont = 0

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    circuit = QuantumCircuit(5, 5)
                    if i == 1:
                        circuit.x(0)
                    if j == 1:
                        circuit.x(1)
                    if k == 1:
                        circuit.x(2)
                    if l == 1:
                        circuit.x(3)
                    if m == 1:
                        circuit.x(4)
                    circuit.barrier()
                    circuit.barrier()
                    circuit.measure([0,1,2,3,4],[4,3,2,1,0])
                    circuit.barrier()

                    compiled_circuit = transpile(circuit, simulator)

                    job = simulator.run(compiled_circuit, shots=1000)

                    result = job.result()

                    counts = result.get_counts(circuit)

                    for z in counts:
                        mat1[converbi(z)][cont] = 1
                    cont += 1
printm(mat1)


##FUNCION BALANCEADA##
print("Funcion 2")
print("0000--->0")
print("0001--->0")
print("0010--->0")
print("0011--->0")
print("0100--->0")
print("0101--->0")
print("0110--->0")
print("0111--->0")
print("1000--->1")
print("1001--->1")
print("1010--->1")
print("1011--->1")
print("1100--->1")
print("1101--->1")
print("1110--->1")
print("1111--->1")

mat2 = [[0 for k in range(2**(5))] for l in range(2**(5))]

cont = 0

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    circuit = QuantumCircuit(5, 5)
                    if i == 1:
                        circuit.x(0)
                    if j == 1:
                        circuit.x(1)
                    if k == 1:
                        circuit.x(2)
                    if l == 1:
                        circuit.x(3)
                    if m == 1:
                        circuit.x(4)
                    circuit.barrier()
                    circuit.cnot(0,4)
                    circuit.barrier()
                    circuit.measure([0,1,2,3,4],[4,3,2,1,0])
                    circuit.barrier()

                    compiled_circuit = transpile(circuit, simulator)

                    job = simulator.run(compiled_circuit, shots=1000)

                    result = job.result()

                    counts = result.get_counts(circuit)

                    for z in counts:
                        mat2[converbi(z)][cont] = 1
                    cont += 1
printm(mat2)

##FUNCION BALANCEADA##
print("Funcion 3")
print("0000--->0")
print("0001--->0")
print("0010--->0")
print("0011--->0")
print("0100--->1")
print("0101--->1")
print("0110--->1")
print("0111--->1")
print("1000--->0")
print("1001--->0")
print("1010--->0")
print("1011--->0")
print("1100--->1")
print("1101--->1")
print("1110--->1")
print("1111--->1")

mat3 = [[0 for k in range(2**(5))] for l in range(2**(5))]

cont = 0

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    circuit = QuantumCircuit(5, 5)
                    if i == 1:
                        circuit.x(0)
                    if j == 1:
                        circuit.x(1)
                    if k == 1:
                        circuit.x(2)
                    if l == 1:
                        circuit.x(3)
                    if m == 1:
                        circuit.x(4)
                    circuit.barrier()
                    circuit.cnot(1,4)
                    circuit.barrier()
                    circuit.measure([0,1,2,3,4],[4,3,2,1,0])
                    circuit.barrier()

                    compiled_circuit = transpile(circuit, simulator)

                    job = simulator.run(compiled_circuit, shots=1000)

                    result = job.result()

                    counts = result.get_counts(circuit)

                    for z in counts:
                        mat3[converbi(z)][cont] = 1
                    cont += 1
printm(mat3)

##FUNCION BALANCEADA##
print("Funcion 4")
print("0000--->0")
print("0001--->0")
print("0010--->1")
print("0011--->1")
print("0100--->0")
print("0101--->0")
print("0110--->1")
print("0111--->1")
print("1000--->0")
print("1001--->0")
print("1010--->1")
print("1011--->1")
print("1100--->0")
print("1101--->0")
print("1110--->1")
print("1111--->1")

mat4 = [[0 for k in range(2**(5))] for l in range(2**(5))]

cont = 0

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    circuit = QuantumCircuit(5, 5)
                    if i == 1:
                        circuit.x(0)
                    if j == 1:
                        circuit.x(1)
                    if k == 1:
                        circuit.x(2)
                    if l == 1:
                        circuit.x(3)
                    if m == 1:
                        circuit.x(4)
                    circuit.barrier()
                    circuit.cnot(2,4)
                    circuit.barrier()
                    circuit.measure([0,1,2,3,4],[4,3,2,1,0])
                    circuit.barrier()

                    compiled_circuit = transpile(circuit, simulator)

                    job = simulator.run(compiled_circuit, shots=1000)

                    result = job.result()

                    counts = result.get_counts(circuit)

                    for z in counts:
                        mat4[converbi(z)][cont] = 1
                    cont += 1
printm(mat4)