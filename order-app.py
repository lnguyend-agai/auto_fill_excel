import pandas as pd
import datetime

now = datetime.datetime.now()
day_of_week_name = now.strftime("%A")

dict_day = {
    'Monday' : 'Thứ 2',
    'Tuesday': 'Thứ 3',
    'Wednesday': 'Thứ 4',
    'Thursday': 'Thứ 5',
    'Friday': 'Thứ 6'
}

list_name = ['Lộc', 'Bảo', 'David', 'Bao', 'Khiem']
maping_name = {
    'DUC' : 'A.Đức',
    'KHIEM': 'A.Khiêm',
    'BAO': 'Baro'
}
new_list = [maping_name.get(name.upper(), name) for name in list_name]
current_day = dict_day[day_of_week_name]

# Step 1: Read the existing Excel file
file_path = 'C:\\Users\\PC\\Desktop\\customer_test.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Display the original data
print("Original Data:")
print(df)


# Define the column name, row name, and new value
row_name = 'Bảo'
price = '30'

# Check if the specified column and row name exist
for name in list_name:
    if name in df['Tên'].values:
        # Update the value in the specific cell
        df.loc[df['Tên'] == name, current_day] = price

        # Save the updated DataFrame back to the Excel file
        df.to_excel(file_path, index=False)

print("\nUpdated DataFrame:")
print(df)

