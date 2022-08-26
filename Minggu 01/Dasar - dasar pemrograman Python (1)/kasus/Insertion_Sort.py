def insertion_sort(list):
    n = len(list)
    for i in range (1, n):
        key_item = list[i]
        j = i - 1
        
        while j >= 0 and list[j] > key_item:
            list[j+1] = list[j]
            j = j - 1
        
        list[j + 1] = key_item
        
    return list

list = [66, 21, 91, 37, 77, 86, 54]
print(list, "\nSetelah diurutkan")
print(insertion_sort(list))