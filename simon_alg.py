# サイモンのアルゴリズム秘密キーs=11
# 量子回路をふたつつくって比較をおこなう
from qiskit import * 
from qiskit.tools.visualization import plot_histogram, circuit_drawer

def s_oracle(qci, x0,x1,f_x0,f_x1):
    qci.x(f_x1)
    qci.cx(x0,f_x0)
    qci.cx(x1,f_x0)
    
bn=4 #量子ビット数

cn=2 #古典ビット数

q = QuantumRegister(bn) #bn個の 量子 レジスタqの 生成 
c = ClassicalRegister(cn) #cn個の 古典 的 レジスタcの 生成 
qc = QuantumCircuit(q, c) #量子 回路 qc1の 生成 

# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

# アダマールゲートでそれぞれのビットに対して、重ね合わせ状態を生成する
for i in range(cn):
    qc.h(q[i])

# サイモン問題の量子オラクル
s_oracle(qc,q[0],q[1],q[2],q[3])    

# アダマールゲートでそれぞれのビットに対して、重ね合わせ状態を生成する
for i in range(bn):
    qc.h(q[i])

# 量子測定
for i in range(cn):
    qc.measure(q[cn-1-i], c[i])

# 量子ゲート部分　＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=8192).result()
rc = r.get_counts()
print(rc)
# circuit_drawer(qc)
plot_histogram(rc)

# 測定ビット|y>=|y0y1>として、|00>と|11>とがそれぞれほぼ
# 50%の確率で観測されたことになる
