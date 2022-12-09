'''3) Реализовать функцию my_func(), которая принимает.
 три позиционных аргумента, и возвращает сумму наибольших двух аргументов '''
def my_func(*args):
    b = sorted(list(args))
    print(b)
    addition = b[1] + b[2]
    print(addition)


my_func(10, 7, 10)


# def get_max(*args):
#   print(sum(sorted(list(args), reverse=True)[:2]))
#get_max(-70, 50, 70)

# def get_max(*args):
#   ist = list(args)
#   i = 0
#   res = 0
#   while i != 2:
#       max_val = max(ist)
#       res += max_val
#       ist.remove(max_val)
#       i += 1
#   print(res)
# get_max(-70,50,70)         
