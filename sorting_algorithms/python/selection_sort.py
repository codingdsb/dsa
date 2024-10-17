def selection_sort(numbers):

    for n in range(len(numbers)-1):
        min_num = numbers[n]
        min_num_index = n
        for i in range(n, len(numbers)):
            if numbers[i] < min_num:
                min_num = numbers[i]
                min_num_index =  i
        numbers[n], numbers[min_num_index] = numbers[min_num_index], numbers[n]
    return numbers
