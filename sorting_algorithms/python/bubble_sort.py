def bubble_sort(numbers):
    for n in range(len(numbers)-1):
        swaps = 0
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                swaps += 1
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        if swaps == 0:
            break

    return numbers
