# Final Project

## Taylor Series Approximation of sin(x) Using Python

本專題使用泰勒級數（麥克勞林級數）來逼近 sin(x) 函數，並分析不同項數對逼近效果的影響。

## 數學背景

sin(x) 在 x = 0 處的麥克勞林級數：

$$
\sin(x) = \sum_{i=0}^{\infty} \frac{(-1)^i}{(2i+1)!} x^{2i+1} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots
$$

## 實作方法

- 使用 **NumPy** 進行向量化運算
- 使用 **SciPy** 的 `factorial` 函數計算階乘
- 使用 **Matplotlib** 繪製函數曲線與誤差圖

主要函數：
- `taylor_sin(x, n_terms)`：計算泰勒級數逼近值
- `calculate_absolute_error()`：計算絕對誤差

## 結果分析

- **項數越多，逼近範圍越大**：n=1 項僅在 x≈0 附近準確，n=8 項可在整個 [-2π, 2π] 範圍內良好逼近
- **誤差特性**：在 x=0 附近誤差極小（約 10⁻¹⁵），隨著 |x| 增大，誤差呈指數級增長

## 執行方式

```bash
# 安裝依賴套件
pip install -r requirements.txt

# 執行程式
python main.py
```

執行後會生成 `result.png` 圖表（包含函數比較圖和誤差分析圖）。

## 檔案說明

- `main.py`：主程式碼
- `project.py`：擴展版本（更多分析功能）
- `result.png`：分析圖表
- `requirements.txt`：Python 套件依賴清單
