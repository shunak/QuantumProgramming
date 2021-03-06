## 乱数生成による量子ゲート選択

from qiskit import *
from qiskit.tools.visualization import plot_histogram
from numpy.random import * #乱数生成のためのライブラリインポート

q = QuantumRegister(1)  # １つの 量子 レジスタqの 生成
c = ClassicalRegister(1)  # １つの 古典 的 レジスタcの 生成
qc = QuantumCircuit(q, c)  # 量子 回路 qcの 生成

if rand() > 0.5:
    qc.x(q[0])

qc.measure(q, c)  # 量子 レジスタqを 測 定 して 古典 的 レジスタcに 入 れる
#量子 回路 を 実 行 し、 結 果 rに 代入 する
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')
r = execute(qc, backend_sim, shots=100).result()
#量子 回路 名 cnの 量子 プログラムの 実 行 結 果 rからカウント 結 果 取得 し 表示 する
rc = r.get_counts()
print(rc)
plot_histogram(rc)

## この計算結果は、{'0':100}のときもあれば{'1':100}のときもあり、乱数でビット反転演算Xの量子ゲートが選択されていることがわかります。
