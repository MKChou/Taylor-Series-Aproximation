import numpy as np
from scipy.special import factorial
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Microsoft YaHei', 'Arial Unicode MS', 'Noto Sans CJK TC']
plt.rcParams['axes.unicode_minus'] = False

def taylor_sin(x, n_terms):
    result = np.zeros_like(x)
    for k in range(n_terms):
        term = (-1)**k * np.power(x, 2*k + 1) / factorial(2*k + 1)
        result += term
    return result

def calculate_absolute_error(x, true_value, approx_value):
    return np.abs(true_value - approx_value)

def main():
    x = np.linspace(-2*np.pi, 2*np.pi, 1000)
    true_sin = np.sin(x)
    n_terms_list = [1, 3, 5, 8]
    approximations = {}
    for n in n_terms_list:
        approximations[n] = taylor_sin(x, n)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    ax1.plot(x, true_sin, 'k-', linewidth=2.5, label='True sin(x)', zorder=10)
    colors = ['red', 'blue', 'green', 'orange']
    for i, n in enumerate(n_terms_list):
        ax1.plot(x, approximations[n], '--', 
                linewidth=1.5, color=colors[i], 
                label=f'Taylor Series (n={n} terms)', alpha=0.8)
    ax1.set_xlabel('x', fontsize=12)
    ax1.set_ylabel('y', fontsize=12)
    ax1.set_title('Taylor Series Approximation of sin(x)', fontsize=14, fontweight='bold')
    ax1.legend(loc='best', fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
    ax1.axvline(x=0, color='gray', linestyle='-', linewidth=0.5)
    for i, n in enumerate(n_terms_list):
        error = calculate_absolute_error(x, true_sin, approximations[n])
        error = np.maximum(error, 1e-15)
        ax2.semilogy(x, error, '--', 
                    linewidth=1.5, color=colors[i], 
                    label=f'絕對誤差 (n={n} 項)', alpha=0.8)
    ax2.set_xlabel('x', fontsize=12)
    ax2.set_ylabel('絕對誤差 (對數尺度)', fontsize=12)
    ax2.set_title('絕對誤差隨 x 變化（對數尺度）', fontsize=14, fontweight='bold')
    ax2.legend(loc='best', fontsize=10)
    ax2.grid(True, alpha=0.3, which='both')
    ax2.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
    ax2.axvline(x=0, color='gray', linestyle='-', linewidth=0.5)
    plt.tight_layout()
    plt.savefig('result.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()

