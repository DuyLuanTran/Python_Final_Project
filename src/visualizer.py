import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualizer:
    """
    Class Visualizer: Vẽ biểu đồ từ dữ liệu đã làm sạch.
    Yêu cầu: Tên cột phải ở dạng snake_case (vd: math_score) khớp với DataCleaner.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df
        sns.set_style("whitegrid")
        plt.rcParams.update({'font.size': 11})

    def show_score_distribution(self, score_col: str):
        """
        Vẽ Histogram phân phối điểm số.
        """
        if score_col not in self.df.columns:
            print(f"Lỗi: Không tìm thấy cột '{score_col}'")
            return

        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.df, x=score_col, bins=15, kde=True, edgecolor='black')
        plt.title(f"Phân phối điểm: {score_col}", fontweight='bold')
        plt.tight_layout()
        plt.show()

    def show_comparison_box(self, x_col: str, y_col: str):
        """
        Vẽ Boxplot so sánh điểm số (y_col) giữa các nhóm (x_col).
        """
        if x_col not in self.df.columns or y_col not in self.df.columns:
            print(f"Lỗi: Không tìm thấy cột '{x_col}' hoặc '{y_col}'")
            return

        plt.figure(figsize=(12, 6))
        sns.boxplot(data=self.df, x=x_col, y=y_col, palette="Set2")
        plt.title(f"So sánh {y_col} theo {x_col}", fontweight='bold')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def show_correlation_heatmap(self):
        """
        Vẽ Heatmap tương quan giữa các môn học (tự động lấy các cột số).
        """
        target_cols = ["math_score", "reading_score", "writing_score", "average_score"]
        existing_cols = [c for c in target_cols if c in self.df.columns]

        if len(existing_cols) < 2:
            print("Cảnh báo: Không đủ cột số liệu để vẽ tương quan.")
            return

        plt.figure(figsize=(8, 6))
        sns.heatmap(self.df[existing_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Ma trận tương quan", fontweight='bold')
        plt.tight_layout()
        plt.show()

    def show_grade_rank_count(self):
        """
        Vẽ biểu đồ đếm số lượng theo xếp loại (yêu cầu cột grade_rank).
        """
        if "grade_rank" not in self.df.columns:
            print("Lỗi: Chưa có cột 'grade_rank'. Hãy chạy DataCleaner trước.")
            return

        rank_order = ["Excellent", "Good", "Average", "Poor"]
        
        plt.figure(figsize=(8, 5))
        sns.countplot(data=self.df, x="grade_rank", order=rank_order, palette="viridis", edgecolor="black")
        plt.title("Số lượng học sinh theo xếp loại", fontweight='bold')
        plt.tight_layout()
        plt.show()

    def show_pairplot(self, hue_col: str):
        """
        Vẽ Pairplot tổng quan phân theo nhóm màu (hue_col).
        """
        score_cols = ["math_score", "reading_score", "writing_score"]
        
        if hue_col not in self.df.columns:
            print(f"Lỗi: Không tìm thấy cột '{hue_col}'")
            return

        sns.pairplot(self.df, vars=score_cols, hue=hue_col, palette="husl", diag_kind="kde")
        plt.show()
