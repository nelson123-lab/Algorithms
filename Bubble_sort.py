n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
count = 0
def sort1(lst):
    #Bubble sort 
    global count
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                count += 1
                t = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = t

sort1(a)
print("Array is sorted in "+ str(count) + " swaps.")
print("First Element: "+ str(a[0]))
print("Last Element: " + str(a[-1]))
print("Sorted array", a)

"""
INPUT 

n = 5
a = 4 6 2 1 8

OUTPUT

Array is sorted in 5 swaps.
First Element: 1
Last Element: 8
Sorted array [1, 2, 4, 6, 8]

"""
