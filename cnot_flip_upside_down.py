## アダマール変換による制御NOTゲートの上下反転

from qiskit import *
from qiskit.tools.visualization import plot_histogram

bn = 2  # ビット数

q = QuantumRegister(bn)  # １つの 量子 レジスタqの 生成
c = ClassicalRegister(bn)  # １つの 古典 的 レジスタcの 生成
qc = QuantumCircuit(q, c)  # 量子 回路 qcの 生成

qc.h(q[0])
qc.x(q[1])
qc.h(q[1])
qc.cx(q[0], q[1])
qc.h(q[0])
qc.h(q[1])

for i in range(bn):
    qc.measure(q[bn-1-i], c[i])

#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=8192).result()
rc = r.get_counts()
print(rc)
plot_histogram(rc)

# 結果、入力ビット|01>に対して、出力ビット|11>となっているので、
# あたかも制御NOTゲートが逆転した結果になっている
