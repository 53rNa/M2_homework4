# Задание "Слишком древний шифр"

import random

rand_num = random.randint(3, 20) # Генерируем число от 3 до 20
number_list = []
i = 1
while i <= rand_num:
    j = i + 1                                        # Формируем пары чисел
    while j <= rand_num:
        sum = i + j                                  # Вычисляем сумму этих чисел

        # проверяем кратно (делится ли без остатка) ли сгенерированное число этой сумме
        if sum != 0 and rand_num % sum == 0:         # Записываем в список только нужную пару чисел
            number_list.append(i)
            number_list.append(j)
        j += 1
    i += 1

result = ''.join(map(str, number_list))
print (rand_num, '- число из первой вставки')
print (result, '- нужный пароль')
