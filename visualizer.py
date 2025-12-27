import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def grade_rank_distribution(df: pd.DataFrame, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))

    rank_counts = df['grade_rank'].value_counts()
    ranks = rank_counts.index
    counts = rank_counts.values

    ax.bar(ranks, counts, color='skyblue')
    ax.set_title("Phân phối Xếp loại Học lực")
    ax.set_xlabel("Xếp loại")
    ax.set_ylabel("Số lượng")


def average_score_histogram(df: pd.DataFrame, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))

    ax.hist(df["average_score"], bins='auto', color='#a8dadc', edgecolor='black', alpha=0.7)
    ax.set_ylabel("Số lượng (Count)", color='black')

    ax2 = ax.twinx()
    sns.kdeplot(df["average_score"], color='#e63946', linewidth=2, ax=ax2)
    ax2.set_ylabel("Mật độ (Density)", color='#e63946')

    ax.set_title("Phân phối điểm trung bình (Histogram + KDE)")
    ax.set_xlabel("Điểm trung bình")


def grouped_bar_chart(df: pd.DataFrame, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))

    counts = pd.crosstab(df['grade_rank'], df['gender'])

    valid_ranks = [r for r in ['Excellent', 'Good', 'Average', 'Poor'] if r in counts.index]
    counts = counts.reindex(valid_ranks)

    counts.plot(kind='bar', ax=ax, rot=0)
    ax.set_title("Tương quan Xếp loại theo Giới tính")
    ax.set_xlabel("Xếp loại")
    ax.set_ylabel("Số lượng")

def plot_manual_pairplot(df: pd.DataFrame, axes_grid=None):
    cols = ['math_score', 'reading_score', 'writing_score']
    ranks = ['Excellent', 'Good', 'Average', 'Poor']

    color_map = {'Excellent': '#2ca02c', 'Good': '#1f77b4', 'Average': '#ff7f0e', 'Poor': '#d62728'}
    n = len(cols)

    if axes_grid is None:
        fig, axes_grid = plt.subplots(nrows=n, ncols=n, figsize=(12, 12))

    for i in range(n):
        for j in range(n):
            ax = axes_grid[i, j]
            y_var = cols[i]
            x_var = cols[j]

            for rank in ranks:
                if rank not in df['grade_rank'].unique(): continue

                subset = df[df['grade_rank'] == rank]
                color = color_map.get(rank, 'gray')

                if i == j:
                    ax.hist(subset[x_var], bins=15, alpha=0.5, color=color, label=rank)
                else:
                    ax.scatter(subset[x_var], subset[y_var], color=color, s=20, alpha=0.6, label=rank)

            if i == n - 1:
                ax.set_xlabel(x_var)
            else:
                ax.set_xlabel('')
            if j == 0:
                ax.set_ylabel(y_var)
            else:
                ax.set_ylabel('')

            if i == 0 and j == 0:
                ax.legend(title="Xếp loại", fontsize='x-small')

def create_dashboard(df: pd.DataFrame):
    fig = plt.figure(figsize=(18, 14))
    fig.suptitle('DASHBOARD PHÂN TÍCH HỌC LỰC HỌC SINH', fontsize=20, weight='bold')

    gs = fig.add_gridspec(4, 3, height_ratios=[1, 1, 1, 1])

    ax1 = fig.add_subplot(gs[0, 0])
    grade_rank_distribution(df, ax=ax1)

    ax2 = fig.add_subplot(gs[0, 1])
    average_score_histogram(df, ax=ax2)

    ax3 = fig.add_subplot(gs[0, 2])
    grouped_bar_chart(df, ax=ax3)

    pairplot_axes = np.empty((3, 3), dtype=object)

    for i in range(3):
        for j in range(3):
            pairplot_axes[i, j] = fig.add_subplot(gs[i + 1, j])

    plot_manual_pairplot(df, axes_grid=pairplot_axes)

    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Chừa chỗ cho tiêu đề lớn
    plt.show()