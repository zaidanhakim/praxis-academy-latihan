def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range (n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list [j + 1] = list[j + 1], list[j]
    return list


list = [5, 3, 4, 8, 1, 2, 9, 6, 15, 7]
print(list, "\nSetelah diurutkan")
print(bubble_sort(list))