import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

simulator = Aer.get_backend('qasm_simulator')

print("Funcion 1")
print("0--->1")
print("1--->1")

for i in range(2):
    for j in range(2):
        print("Results for",i,j)
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

        print("\nTotal count for 00 and 11 are:",counts)

        print(circuit)

        plot_histogram(counts)

        plt.show()

print("Funcion 2")
print("0--->0")
print("1--->1")

for i in range(2):
    for j in range(2):
        print("Results for",i,j)
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

        print("\nTotal count for 0 and 1 are:",counts)

        print(circuit)

        plot_histogram(counts)

        plt.show()


print("Funcion 3")
print("0--->1")
print("1--->0")

for i in range(2):
    for j in range(2):
        print("Results for",i,j)
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

        print("\nTotal count for 0 and 1 are:",counts)

        print(circuit)

        plot_histogram(counts)

        plt.show()

print("Funcion 4")
print("0--->0")
print("1--->0")

for i in range(2):
    for j in range(2):
        print("Results for",i,j)
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

        print("\nTotal count for 0 and 1 are:",counts)

        print(circuit)

        plot_histogram(counts)

        plt.show()