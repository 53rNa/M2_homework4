
# Задача "Матрица воплоти"
def get_matrix (n, m, value):
    matrix = []                             # создание пустого списка matrix
    for i in range(n):                      # количество строк матрицы
        matrix.append([])                   # добавляем пустой список в список matrix
        for j in range(m):                  # количество столбцов матрицы
            matrix[i].append(value)         # Записываем в список значение
    return (matrix)                         # возвращение значения переменной matrix функции get_matrix

result1 = get_matrix(2, 2, 10)  # Вывод результата работы функции get_matix
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
