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
            
list = [100, 23, 34, 98, 24, 56, 72, 11, 63, 120, 99]
print(list, "\nsetelah diurutkan")
print(merge_sort(list))