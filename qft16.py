# |0000>の量子フーリエ変換QFT16
from qiskit import *
from qiskit.tools.visualization import plot_histogram, circuit_drawer
import math
def qft(qci, q, n):
    for i in range(n):
        for j in range(i): qci.cu1(math.pi/float(2**(i-j)), q[i], q[j])
        qci.h(q[i])


bn=4 # 量子ビット数

# 制御回転ゲートは制御ビットと目標ビットを入れ替えても同じ
# n=0
# for j in range(0): qci.cu1(math.pi/float(2**(0-0)), q[0], q[0])
# n=1
# for j in range(1): qci.cu1(math.pi/float(2**(1-0)), q[1], q[0])
# n=2
# for j=0 in range(2): qci.cu1(math.pi/float(2**(2-0)), q[2], q[0])
# for j=1 in range(2): qci.cu1(math.pi/float(2**(2-1)), q[2], q[1])
# n=3
# for j=0 in range(3): qci.cu1(math.pi/float(2**(3-0)), q[3], q[0])
# for j=1 in range(3): qci.cu1(math.pi/float(2**(3-1)), q[3], q[1])
# for j=2 in range(3): qci.cu1(math.pi/float(2**(3-2)), q[3], q[2])


q = QuantumRegister(bn) #ba個の 量子 レジスタqの 生成
c = ClassicalRegister(bn) #bn個の 古典 的 レジスタcの 生成
qc = QuantumCircuit(q, c) #量子回路の生成
# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

qft(qc,q,bn)
for i in range(bn):
    qc.measure(q[bn-1-i],c[i])

# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=8192).result()
rc = r.get_counts()
print(rc)
# circuit_drawer(qc)
plot_histogram(rc)




