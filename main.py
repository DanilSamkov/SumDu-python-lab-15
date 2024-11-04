import pandas as pd

# Створення DataFrame з даними
data = {
    "Vitaly_Prikhodko": [12, 10, 9, 10, 5, 7, 8, 5, 12, 10],
    "Dmytro_Kropyvnytskyi": [12, 10, 9, 5, 6, 7, 4, 3, 12, 4],
    "Mikhail_Romanenko": [12, 3, 4, 6, 5, 5, 3, 7, 5, 4]
}

df = pd.DataFrame(data)

# Вивід початкового DataFrame
print("Початковий DataFrame:")
print(df)

# Функція для видалення повторень у стовпці
def remove_duplicates(series):
    return pd.Series(series.drop_duplicates().tolist())

# Функція для пошуку перших п'яти мінімальних елементів
def get_top_5_min(series):
    sorted_values = sorted(series.dropna())
    return sorted_values[:5]

# Видалення повторень для кожного стовпця
unique_scores = df.apply(remove_duplicates)

# Вивід DataFrame з унікальними значеннями
print("\nDataFrame з унікальними значеннями:")
print(unique_scores)

# Пошук перших п'яти мінімальних елементів для кожного стовпця
top_5_min = unique_scores.apply(get_top_5_min)

# Вивід перших п'яти мінімальних елементів
print("\nПерші п'ять мінімальних елементів:")
print(top_5_min)
