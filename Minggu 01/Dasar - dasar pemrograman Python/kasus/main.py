from Module_Sorting import *

#quick sort
list = [50, 30, 45, 66, 78, 23, 90, 59]
print("\nlist sebelum diurutkan\n",list, "\nsetelah diurutkan dengan quick sort")
print(quick_sort(list), "\n")

#selection sort
list = [64, 25, 12, 22, 11, 99]
print("list sebelum diurutkan\n",list, "\nSetelah diurutkan dengan selection sort")
print(selection_sort(list), "\n")

#merge sort
list = [100, 23, 34, 98, 24, 56, 72, 11, 63, 120, 99]
print("list sebelum diurutkan\n",list, "\nsetelah diurutkan dengan merge sort")
print(merge_sort(list), "\n")

#bubble sort
list = [5, 3, 4, 8, 1, 2, 9, 6, 15, 7]
print("list sebelum diurutkan\n",list, "\nSetelah diurutkan dengan bubble sort")
print(bubble_sort(list), "\n")

#insertion sort
list = [66, 21, 91, 37, 77, 86, 54]
print("list sebelum diurutkan\n",list, "\nSetelah diurutkan dengan insertion sort")
print(insertion_sort(list), "\n")