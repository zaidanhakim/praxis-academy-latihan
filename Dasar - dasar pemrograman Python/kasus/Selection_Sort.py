def selection_sort(list):  
    n = len(list)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if list[min_index] > list[j]:
                min_index = j
                
        list[i], list[min_index] = list[min_index], list[i]
    return list

list = [64, 25, 12, 22, 11, 99]
print(list, "\nSetelah diurutkan")
print(selection_sort(list))