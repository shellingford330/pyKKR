# What is this?

Kernel Kalman rule (KKR) のプログラム（Python）と[Kernel Kalman ruleの論文](https://link.springer.com/content/pdf/10.1007/s10994-019-05816-z.pdf)で行っている実験（Jupyter Notebook）

## Environment

- Python: 3.9

## Setup

1. Install Anaconda

[公式サイト](https://www.anaconda.com/products/individual)からAnacondaをインストール

2. Launch Jupyter Notebook

## Directory structure

```
.
├── kkr
│   ├── __init__.py
│   ├── environments ・・・ シミュレートする環境
│   │   └──  Pendulum.py ・・・ 振り子の状態モデル
│   ├── kernels ・・・ カーネルに関するライブラリ
│   ├── filter.py ・・・　Kernel Bayes Filter (KBF(a), KBF(b), KBF(c)), Kernel Kalman Filter (KKF)
│   ├── preprocessors.py　・・・ データの整形ライブラリ
│   ├── simulator.py　・・・ シミュレーター
│   └── smoother.py ・・・ Kernel　Forward　Backward　Smoother （KFBS）
└── notebooks ・・・　Kernel Kalman ruleの論文で行っている実験
    ├── Comparison　of　KKR,　subKKR,　KBR,　and　subKBR.ipynb　・・・　ガウス分布の期待値推定（論文 4.5節参照）
    └── KKF Example - Pendulum.ipynb ・・・ 振り子の実験(論文 5.3.1節参照)
```
