s1 = input("Введіть перший рядок символів: ")
s2 = input("Введіть другий рядок символів: ")
set1 = set(s1)
set2 = set(s2)
result = set1 - set2
print("Символи, які є у першому рядку і відсутні у другому:")
for char in result:
    print(char, end=" ")
