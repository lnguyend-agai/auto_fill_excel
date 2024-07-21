import pandas as pd
import datetime
from typing import List

def auto_fill(user_list: List[str], file_path: str):
    """
    Auto-fills the specified cells in the Excel file based on the user list and current day.
    """
    new_list = map_user_names(user_list)
    current_day = get_current_day()

    df = pd.read_excel(file_path, engine='openpyxl')

    print("Original Data:")
    print(df)

    update_cells(new_list, current_day, df)
    df.to_excel(file_path, index=False)

    print("\nUpdated DataFrame:")
    print(df)

def update_cells(new_list: List[str], current_day: str, df, price: int = 30):
    """
    Updates the cells in the DataFrame for the specified user names and current day.
    """
    for name in new_list:
        if name in df['Tên'].values:
            df.loc[df['Tên'] == name, current_day] = price

def get_current_day() -> str:
    """
    Returns the current day of the week in Vietnamese.
    """
    now = datetime.datetime.now()
    day_of_week_name = now.strftime("%A")

    day_mapping = {
        'Monday': 'Thứ 2',
        'Tuesday': 'Thứ 3',
        'Wednesday': 'Thứ 4',
        'Thursday': 'Thứ 5',
        'Friday': 'Thứ 6',
        'Saturday': 'Thứ 7',
        'Sunday': 'Chủ nhật'
    }
    return day_mapping[day_of_week_name]

def map_user_names(user_list: List[str]) -> List[str]:
    """
    Maps the user names from the provided list to their corresponding values.
    """
    name_mapping = {
        'LOC': 'Lộc',
        'DUC': 'A.Đức',
        'KHIEM': 'A.Khiêm',
        'BAO': 'Baro',
        'THINH': 'A.Thịnh',
        'TRUNG': 'A.Trung',
        'HIEU': 'A.Hiếu',
        'PHAT': 'A.Phát',
        'TAI': 'A.Tài',
        'CANH': 'Cảnh'
    }
    return [name_mapping.get(name.upper(), name) for name in user_list]
