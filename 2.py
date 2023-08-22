'''
Процедурное программирование:
__
Разбиение массива на подмассивы:
__
Описание: Имеется массив чисел. Необходимо разбить 
его на подмассивы так, чтобы сумма чисел в каждом 
подмассиве была меньше или равна заданному значению X.
Почему это процедурное программирование: Можно создать 
процедуру, которая будет принимать массив и значение X, 
а затем последовательно формировать подмассивы, следуя 
определенной логике. Это позволяет выделить процесс 
создания каждого подмассива в отдельную подпрограмму, 
делая основной код более чистым и понятным.
'''


def search_sum(arr, n_sum):
    sum = 0
    new_arr = []
    current_arr = []
    for el in arr:
        if el > n_sum:
            print("аргумент", el, " превышает назначенную сумму")
        elif sum + el <= n_sum:
            current_arr.append(el)
            sum += el
        else:
            new_arr.append(current_arr)
            current_arr = [el]
            sum = el

    new_arr.append(current_arr)
    return new_arr
    

arr = [11, 2, 3, 4, 5, 16, 7, 8, 9]
n_sum = 10
k = search_sum(arr, n_sum)
print(k)

