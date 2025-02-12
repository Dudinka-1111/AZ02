import pandas as pd

# Создаем данные (10 учеников с оценками учеников по 5 разным предметам)
data = {
    'Имя': ['Алексей', 'Мария', 'Иван', 'Елена', 'Дмитрий', 'Ольга', 'Сергей', 'Анна', 'Павел', 'Наталья'],
    'Математика': [5, 4, 3, 5, 4, 3, 5, 4, 3, 5],
    'Физика': [3, 5, 4, 3, 5, 4, 3, 5, 4, 3],
    'Химия': [4, 3, 5, 4, 3, 5, 4, 3, 5, 4],
    'Литература': [5, 4, 3, 5, 4, 3, 5, 4, 3, 5],
    'История': [3, 5, 4, 3, 5, 4, 3, 5, 4, 3]
}

# 1. Создание DataFrame
df = pd.DataFrame(data)

# 2. Вывод первых строк
print(df.head())
print("\n")

# 3. Средняя оценка по каждому предмету
for subject in ['Математика', 'Физика', 'Химия', 'Литература', 'История']:
    print(f"Средняя оценка по {subject} - {df[subject].mean()}")
print("\n")

# 4. Медианная оценка по каждому предмету
for subject in ['Математика', 'Физика', 'Химия', 'Литература', 'История']:
    print(f"Медианное значение по {subject} - {df[subject].median()}")
print("\n")

# 5. Q1, Q3 и IQR для Математики
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print(f"Q1 по Математике - {Q1_math}")
print(f"Q3 по Математике - {Q3_math}")
print(f"IQR по Математике - {IQR_math}")
print("\n")

# 6. Стандартное отклонение по Математике
for subject in ['Математика', 'Физика', 'Химия', 'Литература', 'История']:
    print(f"Стандартное отклонение по {subject} - {df[subject].std()}")





