import random
import logging

# Работа с логированием
logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)

# Создан файл для логирования
file_handler = logging.FileHandler("log.log")
# Создание форматера отображающего дату, время, имя логгера, уровень и сообщение
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Диалог с пользователем
print('''Здравствуйте, это программа жеребьевки. 
Для того чтобы провести жеребьевку вам необходимо ввести количество(положительное натуральное число) пользователей 
для жеребьевки. 
Далее последствием нажатия клавиши ENTER вам будут выводится соответствующие числа для жеребьевки

''')

while True:
    logger.info('Program started')
    # Ввод данных и проверка на ввод
    try:
        n = int(input('Введите количество пользователей для жеребьевки: '))
    except ValueError:
        print('Данные введены некорректно. Попробуйте снова.')
        logger.error('Incorrect value.')
        continue
    if n <= 0:
        print('Введены некорректные значения. Попробуйте снова.')
        logger.error('Incorrect value.')
        continue
    logger.info(f'User entered value {n}')

    # Создание и заполнение списка чисел от 1 до n
    a = list()
    for i in range(n):
        a.append(i+1)

    # Вывод случайных чисел при помощи удаления уже выпавших
    for i in range(n):
        rand = random.randint(0, len(a) - 1)
        print(a[rand])
        logger.info(f'Displayed number: {a[rand]}')
        a.pop(rand)
        input('Нажмите ENTER для того чтобы вытащить следующее число')

    # Выход из цикла
    break
logger.info('Program done')
input('\nНажмите ENTER чтобы закрыть программу.')
