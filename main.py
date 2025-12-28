import pandas as pd
import numpy as np
import os
import warnings

# Chặn các cảnh báo "FutureWarning"
warnings.simplefilter(action='ignore', category=FutureWarning)

# Import các module của bạn
import data_loader
import data_cleaner
from visualizer import Visualizer

# Tên file dữ liệu
DATA_FILE = "StudentsPerformance.csv"



def main():

    # --- BƯỚC 1: LOAD DỮ LIỆU ---
    print("=" * 30)
    print("1. LOADING DATA")
    print("=" * 30)
    df = data_loader.load_data(DATA_FILE)

    if df is None:
        return

    # --- BƯỚC 2: CLEANING DATA ---
    print("\n" + "=" * 30)
    print("2. CLEANING DATA")
    print("=" * 30)

    df_clean = data_cleaner.clean_data(df)

    # --- BƯỚC 3: VISUALIZATION ---
    print("\n" + "=" * 30)
    print("3. VISUALIZING")
    print("=" * 30)

    viz = Visualizer(df_clean)

    # Các hàm vẽ biểu đồ
    print(">> Đang hiển thị biểu đồ phân phối điểm Toán...")
    viz.show_score_distribution("math_score")

    print(">> Đang hiển thị ma trận tương quan...")
    viz.show_correlation_heatmap()

    print(">> Đang hiển thị xếp loại học lực...")
    viz.show_grade_rank_count()

    if "gender" in df_clean.columns:
        print(">> Đang hiển thị so sánh theo giới tính...")
        viz.show_comparison_box(x_col="gender", y_col="reading_score")
        viz.show_pairplot(hue_col="gender")

    print("\n CHƯƠNG TRÌNH HOÀN TẤT!")


if __name__ == "__main__":
    main()