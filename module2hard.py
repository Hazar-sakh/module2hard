# Слишком древний шифр

# Задаем последовательность и условие для работы программы вычисления

num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_of_true = ['12', '13', '1423', '121524', '162534', '13172635', '1218273645', '141923283746',
                '11029384756', '12131511124210394857', '112211310495867', '1611325212343114105968',
                '1214114232133124115106978', '1317115262143531341251161079', '11621531441351261171089',
                '12151811724272163631545414513612711810', '118217316415514613712811910',
                '13141911923282183731746416515614713812911']
que = 'да'

# Запускаем цикл с проверкой введенного числа при условии для работы

while que == 'да':
  num2 = []  # Создаем пустой список для хранения вычисленных значений
  while num2 == []: # Цикл вычислений повторяется пока список не заполнится значениями
    iter = int(input('Введите число от 3 до 20:\n> ')) #
    if iter >= 3 and iter <= 20: # Ограничиваем ввод чисел от 3 до 20
      for i in num1: # Перебираем числа (из списка num1) для первой цифры пары
        for j in num1: # Перебираем числа (из списка num1) для второй цифры пары
          if i <= j: # Ограничение: первая цифра пары не должна быть больше второй цифры пары
            if iter % (i + (j)) == 0 and j != i: # Проверяем кратность чисел (к заданному занчению) исключаем дублирование
              num2.append(i) # Добавляем первую цифру
              num2.append(j) # Добавляем вторую цифру
    else:
       print('\nВы ввели неверное число\n') # Возвращаемся к вводу значения, если введено неверно
       continue

  # Вывод результата

  print()
  print('Получился пароль: ')
  print(*num2)




  # Проверка результата

  ch = True  # Устанавливаем условие для цикла
  num2 = "".join(str(num2[0]) for num2[0] in num2)  # Преобразуем список в строку

  while ch: 
    rec = input('\nПроверить полученный пароль вручную или автоматически? (Руч/Авто):\n> ')  # Выбираем способ проверки
    rec = rec.lower()  # Правим регистр
    if rec == 'авто':  # Автопроверка
      while ch:
        not_check = True # Флаг неверного результата
        for i in list_of_true: # Перебираем все значения из списка list_of_true
          if i == num2:
            print('\nПароль верный!')
            ch = False
          elif i == len(num2) and not_check:
            print('\nПароль и введенная последовательность не совпадают!')
            ch = False
    elif rec == 'руч':  # Ручная проверка
        check = str(input(f'\n\nВведите последовательность из задания для цифры {iter} (без пробелов и знаков препинания):\n> '))
        if num2 == check:
          print('\nПароль верный!')
          ch = False
        else:
          print('\nПароль и введенная последовательность не совпадают!')
          ch = False
    else:
      print('\nВы ввели неверное значение!')
      continue

  # Повторить?

  Q = True
  while Q:
    que2 = input('\nЖелаете повторить? (Да/Нет):\n> ')
    que2 = que2.lower()
    if que2 == 'да':
      que = que2
      break
    elif que2 == 'нет':
      que = que2
      break
    else:
      print('\nВы ввели неверное значение!')
      continue  
  print('\n\n\n')

# Заврешить

print('Вычисления завершены! Спасибо!')
