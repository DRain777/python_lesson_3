
#7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
#При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
#Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!. 
n = int(input('Введите факториал числа' ))
f = 1
def fact(n,f):

    for i in range(2, n+1):
        f = f * i
        print(f)
        
    


fact(n,f)    