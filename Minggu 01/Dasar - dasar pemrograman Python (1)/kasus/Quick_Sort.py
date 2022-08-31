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

list = [50, 30, 45, 66, 78, 23, 90, 59]
print(list, "\nsetelah diurutkan")
print(quick_sort(list))
