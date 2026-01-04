import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
import matplotlib

try:
    matplotlib.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Microsoft YaHei', 'Arial Unicode MS', 'Noto Sans CJK TC']
    matplotlib.rcParams['axes.unicode_minus'] = False
except:
    pass

def taylor_sin(x, n_terms):
    result = np.zeros_like(x, dtype=np.float64)
    for i in range(n_terms):
        term = ((-1)**i) * (x**(2*i + 1)) / factorial(2*i + 1)
        result += term
    return result

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
sin_true = np.sin(x)
n_terms_list = [1, 3, 5, 7, 9, 15]
approximations = {}

for n in n_terms_list:
    approximations[n] = taylor_sin(x, n)

plt.figure(figsize=(12, 8))
plt.plot(x, sin_true, 'k-', linewidth=2.5, label='真實 sin(x)', zorder=10)
colors = plt.cm.viridis(np.linspace(0, 1, len(n_terms_list)))
for i, n in enumerate(n_terms_list):
    plt.plot(x, approximations[n], '--', 
             color=colors[i], linewidth=1.5, 
             label=f'Taylor (n={n})', alpha=0.8)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('sin(x) 的泰勒級數逼近', fontsize=16, fontweight='bold')
plt.legend(loc='best', fontsize=10)
plt.grid(True, alpha=0.3)
plt.xlim(-2*np.pi, 2*np.pi)
plt.ylim(-1.5, 1.5)
plt.axvline(x=0, color='gray', linestyle=':', alpha=0.5)
plt.axhline(y=0, color='gray', linestyle=':', alpha=0.5)
plt.tight_layout()
plt.savefig('taylor_approximation.png', dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(12, 8))
for i, n in enumerate(n_terms_list):
    error = np.abs(sin_true - approximations[n])
    error_log = np.log10(error + 1e-15)
    plt.plot(x, error_log, '-', 
             color=colors[i], linewidth=2, 
             label=f'誤差 (n={n})', alpha=0.8)
plt.xlabel('x', fontsize=14)
plt.ylabel('log10(絕對誤差)', fontsize=14)
plt.title('泰勒級數逼近的誤差分析（對數尺度）', fontsize=16, fontweight='bold')
plt.legend(loc='best', fontsize=10)
plt.grid(True, alpha=0.3)
plt.xlim(-2*np.pi, 2*np.pi)
plt.axvline(x=0, color='gray', linestyle=':', alpha=0.5)
plt.tight_layout()
plt.savefig('error_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(12, 8))
x_local = np.linspace(-np.pi, np.pi, 1000)
sin_true_local = np.sin(x_local)
plt.plot(x_local, sin_true_local, 'k-', linewidth=2.5, label='真實 sin(x)', zorder=10)
for i, n in enumerate([1, 3, 5, 7, 9]):
    approx_local = taylor_sin(x_local, n)
    plt.plot(x_local, approx_local, '--', 
             color=colors[i], linewidth=1.5, 
             label=f'Taylor (n={n})', alpha=0.8)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('sin(x) 的泰勒級數逼近（局部視圖：[-π, π]）', fontsize=16, fontweight='bold')
plt.legend(loc='best', fontsize=10)
plt.grid(True, alpha=0.3)
plt.xlim(-np.pi, np.pi)
plt.ylim(-1.2, 1.2)
plt.axvline(x=0, color='gray', linestyle=':', alpha=0.5)
plt.axhline(y=0, color='gray', linestyle=':', alpha=0.5)
plt.tight_layout()
plt.savefig('taylor_approximation_local.png', dpi=300, bbox_inches='tight')
plt.close()
