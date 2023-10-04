numbers = input("Введіть цілі числа, розділені пробілами: ")
numbers_list = numbers.split()
result = " ".join(["x=" + num for num in numbers_list])
print(result)
