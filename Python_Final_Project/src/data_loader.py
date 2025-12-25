import pandas as pd
import os

def load_data(filepath):
    """
    Hàm đọc dữ liệu từ file CSV.
    """
    if not os.path.exists(filepath):
        print(f"Lỗi: Không tìm thấy file tại {filepath}")
        return None
    
    try:
        df = pd.read_csv(filepath)
        print("Đọc dữ liệu thành công!")
        print(f"Kích thước dữ liệu: {df.shape}")
        return df
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return None