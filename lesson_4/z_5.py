#5) Реализовать формирование списка, используя функцию range() и возможности генератора. 
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
my_list = [i for i in range(100, 1001, 2)]
my_list_1 =list(range(100, 1001,2)) 
print(my_list_1)