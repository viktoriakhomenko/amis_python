print("Здравствуйте!")#Выводим приветствие
first_num = float(input("Введите первое число:"))#Команда для ввода переменной
second_num = float(input("Введите второе число:"))#Команда для ввода переменной
if first_num > second_num:#задаём такое условие, что вторая переменная менше первой
    num = second_num #вводим новую переменную и приравниваем её к меньшей по условию, второй переменной
else: #В других случаях первая переменная меньше
    num = first_num #Вводим новую переменную, присваиваем ей значение 1 переменной
print("Меньшим является число " + str(num))#вывод результатa
print(input("Нажмите клавишу \"Enter\" для окончания работы программы"))#Команда для окончания программы