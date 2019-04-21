# N=8でのグローバー探索アルゴリズム　2回目のグローバー演算（マーキングターゲット|111>）
from qiskit import *
from qiskit.tools.visualization import *

def ccz(qci, q0, q1, q2):
    qci.h(q2)
    qci.ccx(q0, q1, q2)
    qci.h(q2)

def grover(qci, q0, q1, q2):
    ccz(qci, q0, q1, q2)
    for i in [q0, q1, q2]:
        qci.h(i)
        qci.x(i)
    ccz(qci, q0, q1, q2)    
    for i in [q0, q1, q2]:
        qci.x(i)
        qci.h(i)

bn=3
q = QuantumRegister(bn) #ba個の 量子 レジスタqの 生成 
c = ClassicalRegister(bn) #bn個の 古典 的 レジスタcの 生成 
qc = QuantumCircuit(q, c) #量子回路の生成

# 量子回路
for i in range(bn):
    qc.h(q[i])
    
# Grover演算を2回実行
for i in range(2):
    grover(qc,q[0],q[1],q[2])

# 測定
for i in range(bn):
    qc.measure(q[bn-1-i],c[i])

# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=8192).result()
rc = r.get_counts()
print(rc)
# circuit_drawer(qc)
plot_histogram(rc)



# 2回グローバー演算を行った結果、マーキングした|111>の観測確率は90%程まで
# 向上していることが確認できる。
# それでは、グローバー演算を行えば行うほど観測確率は増加するかというと、
# そういうものでもない。適切な演算回数はきまっていて、それをKとすると、
# K=π√N/4-1/2
# とされている