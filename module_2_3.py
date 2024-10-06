my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # исходный список
count = 0   # задаём счетчик
while count < len(my_list):
    num = my_list[count]    # задаём число из списка
    count = count + 1   # запускаем счетчик
    if num == 0:
        continue    # пропускаем 0
    elif num < 0:
        break
    #else:
    print(num)