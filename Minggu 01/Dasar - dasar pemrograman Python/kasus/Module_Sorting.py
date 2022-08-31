def quick_sort(list):
    n = len(list)
    if n <= 1:
        return list
    else:
        poros = list.pop()
        
    items_greater = []
    items_lower = []
    
    for item in list:
        if item > poros:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [poros] + quick_sort(items_greater)

def selection_sort(list):  
    n = len(list)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if list[min_index] > list[j]:
                min_index = j
                
        list[i], list[min_index] = list[min_index], list[i]
    return list

def merge_sort(list):
    n = len(list)
    if len(list) > 1:
        left_list = list[:len(list)//2]
        right_list = list[len(list)//2:]

        merge_sort(left_list)
        merge_sort(right_list)
        
        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i += 1
                k += 1
            else:
                list[k] = right_list[j]
                j += 1
                k += 1
        
        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1
            
        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1
    return list

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range (n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list [j + 1] = list[j + 1], list[j]
    return list

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