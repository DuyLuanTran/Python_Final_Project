import pandas as pd
import numpy as np


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Chuẩn hóa tên cột:
    - Chữ thường
    - Loại bỏ khoảng trắng dư
    - Thay khoảng trắng bằng dấu gạch dưới
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Loại bỏ các dòng dữ liệu trùng lặp
    """
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]

    print(f"Đã xóa {before - after} dòng trùng lặp")
    return df


def remove_outliers_iqr(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Xử lý ngoại lai (outliers) bằng phương pháp IQR
    Áp dụng cho các cột số được truyền vào
    """
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        before = df.shape[0]
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
        after = df.shape[0]

        print(f"{col}: đã loại {before - after} giá trị ngoại lai")

    return df


def add_average_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tạo cột điểm trung bình của 3 môn
    """
    df["average_score"] = (
        df["math_score"] +
        df["reading_score"] +
        df["writing_score"]
    ) / 3

    return df


def add_grade_rank(df: pd.DataFrame) -> pd.DataFrame:
    """
    Phân loại học lực dựa trên điểm trung bình
    """

    def rank(score):
        if score >= 85:
            return "Excellent"
        elif score >= 70:
            return "Good"
        elif score >= 50:
            return "Average"
        else:
            return "Poor"

    df["grade_rank"] = df["average_score"].apply(rank)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pipeline làm sạch dữ liệu hoàn chỉnh:
    - Chuẩn hóa cột
    - Xóa trùng lặp
    - Xử lý outliers
    - Feature engineering
    """
    df = normalize_columns(df)
    df = remove_duplicates(df)

    score_columns = ["math_score", "reading_score", "writing_score"]
    df = remove_outliers_iqr(df, score_columns)

    df = add_average_score(df)
    df = add_grade_rank(df)

    print("Hoàn tất quá trình làm sạch dữ liệu!")
    return df
