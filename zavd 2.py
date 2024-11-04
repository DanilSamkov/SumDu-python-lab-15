import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, FuncFormatter

file_path = 'comptagevelo2017.csv'
df = pd.read_csv(file_path)

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

df['Month'] = df['Date'].dt.month

# Видалимо зайві колонки, що не є велодоріжками
df_cleaned = df.drop(columns=['Unnamed: 1'])

# Обчислюємо відвідування велодоріжок по місяцях
monthly_usage_per_path = df_cleaned.groupby('Month').sum(numeric_only=True)

# Налаштування для повного відображення таблиці
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

print(monthly_usage_per_path)

monthly_usage = monthly_usage_per_path.sum(axis=1)

# Виведемо датафрейм з підсумками по місяцях без індексів
monthly_usage_df = monthly_usage.reset_index(name="Total Cyclist Count")
monthly_usage_df.columns = ["Місяць", "Загальна кількість велосипедистів"]
monthly_usage_df.sort_values(by="Загальна кількість велосипедистів", ascending=False, inplace=True)
print(monthly_usage_df.to_string(index=False))

# Функція для форматування чисел на осі y
def format_y(value, _):
    return f'{int(value):,}'.replace(',', ' ')

# Побудуємо графік загального використання велодоріжок
plt.figure(figsize=(10, 6))
plt.plot(monthly_usage.index, monthly_usage.values, marker='o', color='b', linestyle='-', linewidth=2)
plt.title("Загальне використання велодоріжок по місяцях (2017)")
plt.xlabel("Місяць")
plt.ylabel("Загальна кількість велосипедистів")
plt.xticks(range(1, 13),
           ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень",
            "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"], rotation=45)
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_y))
plt.grid()
plt.tight_layout()
plt.show()

# Побудуємо графік використання кожної велодоріжки по місяцях
plt.figure(figsize=(12, 8))
for path in monthly_usage_per_path.columns:
    plt.plot(monthly_usage_per_path.index, monthly_usage_per_path[path], marker='o', linestyle='-', linewidth=1, label=path)

plt.title("Використання кожної велодоріжки по місяцях (2017)")
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.xticks(range(1, 13),
           ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень",
            "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"], rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_y))
plt.grid()
plt.tight_layout()
plt.show()


